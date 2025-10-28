from fastapi import FastAPI
from app.api.v1.endpoints import wellness_chat

app = FastAPI(
    title="AI Wellness Coach",
    description="A RAG-based health and wellness assistant",
    version="1.0.0"
)

# Include routes
app.include_router(
    wellness_chat.router,
    prefix="/api/v1/wellness",
    tags=["Wellness Chat"]
)

@app.get("/")
def home():
    return {"message": "Welcome to the AI Wellness Coach API 🚀"}
