from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

#  ENUM 
class ApplicationStatus(str, Enum):
    applied = "applied"
    interview = "interview"
    rejected = "rejected"
    offer = "offer"


#  CREATE 
class ApplicationCreate(BaseModel):
    company: str
    position: str
    status: ApplicationStatus = ApplicationStatus.applied


#  RESPONSE 
class ApplicationResponse(BaseModel):
    id: int
    company: str
    position: str
    status: ApplicationStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


#  UPDATE
class ApplicationStatusUpdate(BaseModel):
    status: ApplicationStatus


#  HISTORY RESPONSE 
class ApplicationStatusHistoryResponse(BaseModel):
    id: int
    application_id: int
    old_status: ApplicationStatus
    new_status: ApplicationStatus
    changed_at: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
