# 🧠 Wellness-RAG-AI-App

An **AI-powered Wellness Assistant** built using **FastAPI**, **OpenAI GPT**, and **Pinecone Vector Database**.  
It provides intelligent health insights, personalized chat interactions, and contextual recommendations based on user data — including emotions, wearable (watch) data, and medical reports.
---
## 🧩 Features Overview

✅ Fetch user emotions, health data, and medical reports  
💬 Chat with an AI wellness assistant (memory-enabled)  
🧠 Summarize user chat history into short insights  
📈 Calculate and explain a personalized health score  
🔍 Retrieve similar context from Pinecone (RAG mechanism)  
🩺 Integrate real-time data from backend health APIs  
---

## 🚀 Live API Documentation

👉 **[View on Render (Swagger UI)](https://wellness-rag-ai-app.onrender.com/docs)**  
<img width="1458" height="854" alt="image" src="https://github.com/user-attachments/assets/13d7d452-5eb0-468c-831d-12cc0c0efc32" />
Access all endpoints and test requests directly in the browser.
1️⃣ /get_info: Fetches and stores user emotions, watch data, and medical reports.
2️⃣ /chat: Rag Chatbot service, handles user wellness chat, and saves conversation history.
3️⃣ /chat-history: Returns full recent chat history for a user.
4️⃣ /chat-summary: Summarizes recent chat interactions & generates a title.
5️⃣ /health-score: Calculates a user’s health score from fetched data, then returns the score & analysis
---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Framework** | FastAPI |
| **AI Model** | OpenAI GPT-4o-mini |
| **Vector Database** | Pinecone |
| **Environment Config** | python-dotenv |
| **API Docs** | Swagger UI (FastAPI built-in) |
| **Deployment** | Render Cloud |

---

## 📁 Project Structure
app/
├── main.py # FastAPI entry point
├── routes/
│ └── api_routes.py # All API endpoints
├── services/
│ └── openai_service.py # Handles GPT logic, health analysis, summarization
├── utils/
│ ├── shared_state.py # In-memory store for all_info & chat_history
│ └── pinecone_utils.py # Pinecone setup and embedding utilities
├── schemas/
│ └── user_data.py # User data model and helper methods


---

## ⚙️ Environment Variables (.env)

Create a `.env` file in the project root directory and add:

```env
# Base Backend URL
BASE_URL=http://wellness-backend-2-2dry.onrender.com

# OpenAI
OPENAI_API_KEY=your_openai_api_key

# Pinecone
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=wellness-index
PINECONE_ENVIRONMENT=us-east-1



