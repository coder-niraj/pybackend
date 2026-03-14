from pydantic import BaseModel, EmailStr, Field
class RegisterValidator(BaseModel):
    name: str=Field(min_length=3,max_length=20)
    email: EmailStr
    password: str=Field(min_length=6,max_length=20)
class LoginValidator(BaseModel):
    email: EmailStr
    password: str=Field(min_length=6,max_length=20)
