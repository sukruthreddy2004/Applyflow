from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List

from database import engine, Base
from deps import get_db
from models import Application, ApplicationStatusHistory
from schemas import (
    ApplicationCreate,
    ApplicationResponse,
    ApplicationStatusUpdate,
    ApplicationStatusHistoryResponse,
)

app = FastAPI()

# CREATE TABLES
Base.metadata.create_all(bind=engine)

#  HEALTH 
@app.get("/")
def health_check():
    return {"status": "ApplyFlow backend is running"}

#  CREATE 
@app.post("/applications", response_model=ApplicationResponse)
def create_application(
    application: ApplicationCreate,
    db: Session = Depends(get_db),
):
    db_app = Application(
    company=application.company,
    position=application.position,
    status=application.status
)

    db.add(db_app)
    db.commit()
    db.refresh(db_app)   
    return db_app

# LIST 
@app.get("/applications", response_model=List[ApplicationResponse])
def list_applications(
    status: Optional[str] = Query(default=None),
    db: Session = Depends(get_db),
):
    query = db.query(Application)

    if status:
        query = query.filter(Application.status == status)

    return query.all()

#  UPDATE STATUS
@app.patch(
    "/applications/{application_id}",
    response_model=ApplicationResponse
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

#  HISTORY 
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
        .filter(ApplicationStatusHistory.application_id == application_id)
        .order_by(ApplicationStatusHistory.changed_at)
        .all()
    )
