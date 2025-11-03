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
---

| # | Endpoint | Method | Description |
|---|-----------|--------|-------------|
| 1️⃣ | `/get_info` | **GET** | Fetches and stores user **emotions**, **wearable health data**, and **medical reports** from external APIs. |
| 2️⃣ | `/chat` | **POST** | Handles **RAG-based AI chat** with memory — provides personalized wellness advice and stores conversation history. |
| 3️⃣ | `/chat-history` | **GET** | Retrieves the **full chat history** for a given user. |
| 4️⃣ | `/chat-summary` | **GET** | Summarizes recent chat interactions and generates a **concise title** capturing the main theme. |
| 5️⃣ | `/health-score` | **GET** | Analyzes fetched data and returns a **personalized health score (0–100)** along with improvement suggestions. |

---

✅ Each endpoint is fully documented in the FastAPI Swagger UI.  
You can test them live without any external tools like Postman.  
Just visit the `/docs` route after running the server.
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







