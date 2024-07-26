from uuid import UUID
from app.models import Users
from app.config import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException
from .chatbot_validator import CreateUserData, UserData,UpdateUserData
from app.helper import format_response, exception_format_response, load_error_details
from typing import List,Dict
error_details = load_error_details('error_details.json')

class ChatbotRouter:
    """Class to handle chabot endpoints."""

    def __init__(self):
        """Initialize ChatbotRouter."""
        self.router = APIRouter(prefix='/v1', tags=["chatbot_router"])

        self.router.post("/user", response_model=UserData)(self.create_user)
        self.router.get("/user/{user_id}", response_model=UserData)(self.get_user)
        self.router.put("/user/{user_id}", response_model=UserData)(self.update_user)
        self.router.get("/all_users", response_model=List[UserData])(self.get_all_users)

    async def get_user(
        self,
        user_id:UUID,
        db: Session = Depends(get_db)
    ):
        try:
            user = db.query(Users).filter(Users.id == user_id).first()
            if user is None:
                error_type = 'user_not_found_error'
                response = exception_format_response(
                    detail_type=error_details[error_type]["detail_type"],
                    msg=error_details[error_type]["msg"],
                    reason=error_details[error_type]["reason"],
                )
                raise HTTPException(
                    status_code=error_details[error_type]["status_code"], detail=[response]
                )
            return user
        

        except HTTPException:
            # Re-raise HTTPException to maintain consistent handling
            raise

        except Exception as e:
            error_type = 'exception_error'
            error_msg = f"An error occurred: {str(e)}"
            error_details[error_type]["reason"].format(error_msg=error_msg)
            response = exception_format_response(
                detail_type=error_details[error_type]["detail_type"], msg=error_details[error_type]["msg"], reason=error_msg
            )
            raise HTTPException(
                status_code=error_details[error_type]["status_code"], detail=[response]
            )


    async def create_user(
        self,
        user_data: CreateUserData,
        db: Session = Depends(get_db)
    ):
        try:
            db_user = db.query(Users).filter(Users.email == user_data.email).first()
            if db_user:
                error_type = 'email_already_registered_error'
                response = exception_format_response(
                    detail_type=error_details[error_type]["detail_type"],
                    msg=error_details[error_type]["msg"],
                    reason=error_details[error_type]["reason"],
                )
                raise HTTPException(
                    status_code=error_details[error_type]["status_code"], detail=[response]
                )
                # raise HTTPException(status_code=400, detail="Email already registered")
            
            create_user = Users(
                username=user_data.username,
                email=user_data.email,
                age=user_data.age,
                phone_number=user_data.phone_number,
                income=user_data.income
            )
            db.add(create_user)
            db.commit()
            db.refresh(create_user)
            return create_user

        except HTTPException:
            # Re-raise HTTPException to maintain consistent handling
            raise

        except Exception as e:
            error_type = 'exception_error'
            error_msg = f"An error occurred: {str(e)}"
            error_details[error_type]["reason"].format(error_msg=error_msg)
            response = exception_format_response(
                detail_type=error_details[error_type]["detail_type"], msg=error_details[error_type]["msg"], reason=error_msg
            )
            raise HTTPException(
                status_code=error_details[error_type]["status_code"], detail=[response]
            )


    async def update_user(
            self,
            user_id: UUID,
            user_data: UpdateUserData,
            db: Session = Depends(get_db)
        ):
            try:
                user = db.query(Users).filter(Users.id == user_id).first()
                if user is None:
                    error_type = 'user_not_found_error'
                    response = exception_format_response(
                        detail_type=error_details[error_type]["detail_type"],
                        msg=error_details[error_type]["msg"],
                        reason=error_details[error_type]["reason"],
                    )
                    raise HTTPException(
                        status_code=error_details[error_type]["status_code"], detail=[response]
                    )

                # Update only the fields provided
                if user_data.username is not None:
                    user.username = user_data.username
                if user_data.email is not None:
                    user.email = user_data.email
                if user_data.age is not None:
                    user.age = user_data.age
                if user_data.phone_number is not None:
                    user.phone_number = user_data.phone_number
                if user_data.income is not None:
                    user.income = user_data.income

                db.commit()
                db.refresh(user)
                return user

            except HTTPException:
                # Re-raise HTTPException to maintain consistent handling
                raise

            except Exception as e:
                error_type = 'exception_error'
                error_msg = f"An error occurred: {str(e)}"
                error_details[error_type]["reason"].format(error_msg=error_msg)
                response = exception_format_response(
                    detail_type=error_details[error_type]["detail_type"], msg=error_details[error_type]["msg"], reason=error_msg
                )
                raise HTTPException(
                    status_code=error_details[error_type]["status_code"], detail=[response]
                )
    async def get_all_users(
        self,
        db: Session = Depends(get_db)
    ):
        try:
            users = db.query(Users).order_by(Users.id).all()
            return users

        except Exception as e:
            error_type = 'exception_error'
            error_msg = f"An error occurred: {str(e)}"
            error_details[error_type]["reason"].format(error_msg=error_msg)
            response = exception_format_response(
                detail_type=error_details[error_type]["detail_type"], msg=error_details[error_type]["msg"], reason=error_msg
            )
            raise HTTPException(
                status_code=error_details[error_type]["status_code"], detail=[response]
            )
