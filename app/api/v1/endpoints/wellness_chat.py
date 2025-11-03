from fastapi import APIRouter, Query, Depends, HTTPException
from app.services.openai_service import chat_with_memory, summarize_chat_history, analyze_health_data
from app.schemas.user_data import get_user
from app.utils.shared_state import all_info, chat_history, prompt_counters
import requests
import os
import datetime

router = APIRouter()

@router.get("/get_info")
async def get_info(access_token: str = Query(..., description="User access token"),
                  user_id: str = Query(..., description="User ID"),
                  room_id: str = Query(..., description="Room ID")):
    """
    Get comprehensive user information including emotions, watch data, and medical reports
    """
    global all_info
    # Construct the URLs for all endpoints
    base_url = os.getenv("BASE_URL")
    emotion_url = f"{base_url}/api/v1/emotions/user/{user_id}"
    watch_url = f"{base_url}/api/v1/health-data/user/{user_id}/debug"
    medical_url = f"{base_url}/api/v1/medical-reports"
    
    # Set up headers with the access token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    # Initialize response dictionary
    result = {
        "status": "success",
        "data": {}
    }

    try:
        # Get emotions data
        emotions_response = requests.get(emotion_url, headers=headers)
        if emotions_response.status_code == 200:
            result["data"]["emotions"] = emotions_response.json()
        else:
            result["data"]["emotions"] = {
                "error": f"Failed with status {emotions_response.status_code}",
                "details": emotions_response.text
            }

        # Get watch data
        watch_response = requests.get(watch_url, headers=headers)
        if watch_response.status_code == 200:
            result["data"]["watch_data"] = watch_response.json()
        else:
            result["data"]["watch_data"] = {
                "error": f"Failed with status {watch_response.status_code}",
                "details": watch_response.text
            }

        # Get medical reports
        medical_response = requests.get(medical_url, headers=headers)

        if medical_response.status_code == 200:
            result["data"]["medical_reports"] = medical_response.json()
        else:
            result["data"]["medical_reports"] = {
                "error": f"Failed with status {medical_response.status_code}",
                "details": medical_response.text
            }
        
        # Store the result and room_id in all_info
        all_info[user_id] = {
            "data": result,
            "room_id": room_id
        }
        return result

    except Exception as e:
        error_response = {
            "status": "error",
            "message": "Failed to fetch data",
            "details": str(e)
        }
        all_info[user_id] = {
            "data": error_response,
            "room_id": room_id
        }
        return error_response



@router.post("/chat")
async def wellness_chat(
    query: str = Query(..., description="User question or message"),
    user_id: str = Query(..., description="User ID")
):
    """
    Chat endpoint for user wellness questions.
    """
    global chat_history
    
    # Get room_id from all_info
    if user_id not in all_info:
        raise HTTPException(
            status_code=400,
            detail="Please call get_info endpoint first to initialize the session"
        )
    
    room_id = all_info[user_id]["room_id"]
    
    # Initialize chat history for user if it doesn't exist
    if user_id not in chat_history:
        chat_history[user_id] = []
    
    # Get AI response
    response = chat_with_memory(query, user_id)
    
    # Increment prompt counter for the room
    if room_id not in prompt_counters:
        prompt_counters[room_id] = 0
    prompt_counters[room_id] += 1
    
    # Create chat data
    chat_data = {
        "query": query,
        "response": response,
        "promptUsed": str(prompt_counters[room_id]),  # Incremented prompt counter. global variable from shared_state.py
        "user_id": user_id,
        "room_id": room_id,
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    # Store the exchange in chat history
    chat_history[user_id].append(chat_data)
    
    # Save to database
    try:
        # Make POST request to DB service
        db_url = f"{os.getenv('DB_SERVICE_URL')}/api/v1/chats"
        requests.post(db_url, json=chat_data)
    except Exception as e:
        print(f"Failed to save chat to database: {str(e)}")
    
    return {
        "query": query,
        "response": response,
        "promptUsed": str(prompt_counters[room_id])
    }

@router.get("/chat-history")
async def get_chat_history(user_id: str = Query(..., description="User ID")):
    """
    Get chat history for a specific user
    """
    user_history = chat_history.get(user_id, [])
    return {
        "user_id": user_id,
        "history": user_history
    }

@router.get("/chat-summary")
async def get_chat_summary(
    user_id: str = Query(..., description="User ID"),
    limit: int = Query(5, description="Number of recent messages to summarize")
):
    """
    Get a summary of recent chat history for a specific user
    """
    user_history = chat_history.get(user_id, [])
    
    # Get the most recent conversations based on limit
    recent_history = user_history[-limit:] if user_history else []
    
    # Generate summary and title
    summary_data = summarize_chat_history(recent_history)
    
    return {
        "user_id": user_id,
        "conversation_count": len(recent_history),
        "title": summary_data["title"],
        "summary": summary_data["summary"],
        "recent_messages": recent_history
    }

@router.get("/health-score")
async def get_health_score(user_id: str = Query(..., description="User ID")):
    """
    Calculate and return a health score based on user's data
    """
    # Get user data from all_info
    user_info = all_info.get(user_id)
    
    if not user_info:
        raise HTTPException(
            status_code=404,
            detail="No health data found for this user. Please fetch user data first using /get_info endpoint."
        )
    
    user_data = user_info["data"]

    # Analyze the health data
    analysis_result = analyze_health_data(user_data)
    
    return {
        "user_id": user_id,
        "health_score": analysis_result["score"],
        "analysis": analysis_result["analysis"],
        "last_updated": user_data.get("timestamp", "Unknown"),
        "data_sources": analysis_result["available_sources"]  # Only show actually available sources
    }


