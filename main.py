import os
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from sqlalchemy import create_engine
from app.config import SessionLocal, create_db_engine
from app.models import Base
from app.chatbot.chatbot import ChatbotRouter
import requests
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

print("DATABASE_URL:::::::::::::::;",DATABASE_URL)

class ChatbotApp(FastAPI):
    def __init__(self):
        super().__init__(
            debug=True,
            docs_url="/v1/docs",
        )

        # Create database engine and metadata
        engine = create_db_engine()
        Base.metadata.create_all(bind=engine)

        # Configure session-maker
        SessionLocal.configure(bind=engine)

        self.chatbot_router = ChatbotRouter()
        # self.create_user = 

        self.include_router(self.chatbot_router.router)

app = ChatbotApp()



@app.get("/v1/ping")
async def ping():
    """Endpoint for server up."""
    return {"message": "Welcome to Chatbot server"}

