from fastapi import APIRouter, Depends
from controller.index import Authentication
from database.index import connectDB
from sqlalchemy.orm import Session

from helpers.index import ApiResponse, UserResponse
from validations.index import LoginValidator, RegisterValidator
router = APIRouter()
authController = Authentication()
@router.post("/",response_model=ApiResponse[UserResponse])
def register(data: RegisterValidator,db: Session = Depends(connectDB)): # type: ignore
    return authController.register(data,db) # type: ignore
@router.post("/login",response_model=ApiResponse[UserResponse])
def login(data: LoginValidator,db: Session = Depends(connectDB)): # type: ignore
    return authController.login(data,db) # type: ignore