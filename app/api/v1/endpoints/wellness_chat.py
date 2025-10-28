from fastapi import APIRouter, Query, Depends
from app.services.openai_service import chat_with_memory
from app.schemas.user_data import get_user
from app.utils.shared_state import all_info
import requests
import os

router = APIRouter()

@router.get("/get_info")
async def get_info(access_token: str = Query(..., description="User access token"),
                  user_id: str = Query(..., description="User ID")):
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
        
        # Store the result in all_info
        all_info[user_id] = result
        return result

    except Exception as e:
        error_response = {
            "status": "error",
            "message": "Failed to fetch data",
            "details": str(e)
        }
        all_info[user_id] = error_response
        return error_response



@router.post("/chat")
async def wellness_chat(query: str = Query(..., description="User question or message")):
    """
    Chat endpoint for user wellness questions.
    """
    response = chat_with_memory(query)
    return {"query": query, "response": response}


