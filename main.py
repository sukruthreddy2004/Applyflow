from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List

from passlib.context import CryptContext

from database import engine, Base
from deps import get_db
from models import User, Application, ApplicationStatusHistory
from schemas import UserLogin, LoginResponse
from schemas import (
    UserCreate,
    UserResponse,
    ApplicationCreate,
    ApplicationResponse,
    ApplicationStatusUpdate,
    ApplicationStatusHistoryResponse,
)


app = FastAPI()


# DATABASE SETUP

Base.metadata.create_all(bind=engine)

# PASSWORD HASHING
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)




# HEALTH CHECK


@app.get("/")
def health_check():
    return {"status": "ApplyFlow backend is running"}



# USER REGISTRATION


@app.post("/users/register", response_model=UserResponse)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    new_user = User(
        email=user.email,
        password_hash=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.post("/users/login", response_model=LoginResponse)
def login_user(
    credentials: UserLogin,
    db: Session = Depends(get_db),
):
    user = (
        db.query(User)
        .filter(User.email == credentials.email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if not verify_password(credentials.password, user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    return {
        "message": "Login successful",
        "user_id": user.id,
        "email": user.email,
    }



# CREATE APPLICATION


@app.post("/applications", response_model=ApplicationResponse)
def create_application(
    application: ApplicationCreate,
    db: Session = Depends(get_db),
):
    db_app = Application(
        company=application.company,
        position=application.position,
        status=application.status,
    )

    db.add(db_app)
    db.commit()
    db.refresh(db_app)

    return db_app


# LIST APPLICATIONS


@app.get("/applications", response_model=List[ApplicationResponse])
def list_applications(
    status: Optional[str] = Query(default=None),
    db: Session = Depends(get_db),
):
    query = db.query(Application)

    if status:
        query = query.filter(Application.status == status)

    return query.all()


# UPDATE APPLICATION STATUS


@app.patch(
    "/applications/{application_id}",
    response_model=ApplicationResponse,
)
def update_application_status(
    application_id: int,
    payload: ApplicationStatusUpdate,
    db: Session = Depends(get_db),
):
    app_record = (
        db.query(Application)
        .filter(Application.id == application_id)
        .first()
    )

    if not app_record:
        raise HTTPException(status_code=404, detail="Application not found")

    old_status = app_record.status
    new_status = payload.status

    app_record.status = new_status

    history = ApplicationStatusHistory(
        application_id=app_record.id,
        old_status=old_status,
        new_status=new_status,
    )

    db.add(history)
    db.commit()
    db.refresh(app_record)

    return app_record



# STATUS HISTORY


@app.get(
    "/applications/{application_id}/history",
    response_model=List[ApplicationStatusHistoryResponse],
)
def get_application_history(
    application_id: int,
    db: Session = Depends(get_db),
):
    return (
        db.query(ApplicationStatusHistory)
        .filter(
            ApplicationStatusHistory.application_id == application_id
        )
        .order_by(ApplicationStatusHistory.changed_at)
        .all()
    )
