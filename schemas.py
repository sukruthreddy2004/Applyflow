from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


# USER SCHEMAS


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


# APPLICATION SCHEMAS


class ApplicationCreate(BaseModel):
    company: str
    position: str
    status: str
    


class ApplicationStatusUpdate(BaseModel):
    status: str


class ApplicationResponse(BaseModel):
    id: int
    company: str
    position: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class PaginatedApplicationsResponse(BaseModel):
    total: int
    page: int
    limit: int
    items: List[ApplicationResponse]


# STATUS HISTORY SCHEMAS


class ApplicationStatusHistoryResponse(BaseModel):
    id: int
    old_status: str
    new_status: str
    changed_at: datetime

    class Config:
        from_attributes = True

# AUTH SCHEMAS

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    message: str
    user_id: int
    email: EmailStr
    access_token: str

