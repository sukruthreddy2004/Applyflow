# ApplyFlow – Job Application Tracking Backend

ApplyFlow is a backend API built with FastAPI, PostgreSQL, and SQLAlchemy to help users track job applications, manage statuses, and maintain application history, all secured with JWT authentication.

This project demonstrates real world backend engineering concepts such as authentication, relational data modeling, password security, and RESTful API design.

 # Key Features
🔐 Authentication & Security

User registration with hashed passwords (bcrypt)

Secure login using JWT (JSON Web Tokens)

Token authentication for protected routes

# Job Application Management

Create job applications linked to users

Track application status (applied, interview, rejected, etc.)

Update application status with full status history tracking

# Relational Database Design

One-to-many relationship:

User → Applications

Application → Status History

PostgreSQL with SQLAlchemy ORM

Automatic timestamps (created_at, updated_at)

# Developer Friendly

Auto generated Swagger UI (/docs)

Clean request & response schemas using Pydantic

Structured project layout (models, schemas, auth, deps)

# Tech Stack

Backend Framework: FastAPI

Database: PostgreSQL

ORM: SQLAlchemy

Authentication: JWT (python-jose)

Password Hashing: passlib (bcrypt)

API Docs: Swagger / OpenAPI

# Project Structure
applyflow-backend/
│
|- main.py          # API routes
|- models.py        # Database models
|- schemas.py       # Pydantic schemas
|- auth.py          # JWT authentication logic
|- database.py      # DB connection setup
|- deps.py          # Dependency injection
|- README.md
|- venv/

# Setup & Installation
1️⃣ Clone the repository
git clone https://github.com/sukruthreddy2004/ApplyFlow.git
cd applyflow-backend

2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure Database

Create a PostgreSQL database and update database.py:

DATABASE_URL = "postgresql+psycopg://username:password@localhost/applyflow"

5️⃣ Run the server
uvicorn main:app --reload

# API Documentation

Once running, open:

 http://127.0.0.1:8000/docs

Swagger UI allows you to:

Register users

Login and get JWT token

Create & manage applications

View application status history

# Authentication Flow (JWT)

Register User

POST /users/register

Login User

POST /users/login

Returns JWT token

Authorized Requests

Send token in header:

Authorization: Bearer <your_token>

# Why This Project Matters

This project demonstrates:

Real authentication 

Secure password handling

Proper database relationships

Backend architecture used in real companies

Debugging 

# Future Improvements

Role based access control

Refresh tokens

Pagination & filtering

Frontend integration (React / Next.js)

Deployment (Railway / Render / AWS)

# Author

Sai Sukruth Reddy
Backend Developer (FastAPI, Python, PostgreSQL)

##  Final Note

This project is built to demonstrate **real backend engineering skills**. It focuses on clean architecture, database integrity, and practical workflows used in production systems.
