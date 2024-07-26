import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_db_engine():
    try:
        # Get DATABASE_URL from environment variables
        database_url = os.getenv("DATABASE_URL")
        print(database_url)
        if database_url is None:
            raise ValueError("DATABASE_URL environment variable is not set")

        # Create and return SQLAlchemy engine
        engine = create_engine(database_url)
        print("Connection established successfully Chatbot Server")
        return engine
    except Exception as error:
        print("Error while connecting to PostgreSQL", error)
        return None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionLocal = sessionmaker(bind=create_db_engine())