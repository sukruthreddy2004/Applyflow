from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    func,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# USER MODEL

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default= func.now())

    applications = relationship("Application", back_populates="user")


# APPLICATION MODEL

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    position = Column(String, nullable=False)
    status = Column(String, nullable=False, default="applied")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="applications")

    history = relationship(
        "ApplicationStatusHistory",
        back_populates="application",
        cascade="all, delete",
    )

# STATUS HISTORY MODEL

class ApplicationStatusHistory(Base):
    __tablename__ = "application_status_history"

    id = Column(Integer, primary_key=True, index=True)

    application_id = Column(
        Integer,
        ForeignKey("applications.id"),
        nullable=False
    )

    old_status = Column(String, nullable=False)
    new_status = Column(String, nullable=False)

    changed_at = Column(DateTime, default=datetime.utcnow)

    application = relationship(
        "Application",
        back_populates="history"
    )
