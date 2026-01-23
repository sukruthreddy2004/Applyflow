#ApplyFlow

ApplyFlow is a backend system for tracking job applications, their statuses, and full status history.
It is built using real world backend practices with secure authentication and relational data modeling.

---

#TECH STACK

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- Passlib (bcrypt)
- Swagger / OpenAPI

---

#FEATURES

##USER AUTHENTICATION
- User registration with hashed passwords
- Secure login using JWT
- Token authentication

##APPLICATION MANAGEMENT
- Create job applications
- Associate applications with users
- Store company, position, and current status

##STATUS TRACKING
- Update application status
- Automatically log every status change
- Maintain complete history

##HISTORY LOG
- Old status -> new status
- Timestamped records
- Per application audit trail

---

#PROJECT STRUCTURE

applyflow-backend/
|
|- main.py             FastAPI routes
|- models.py           SQLAlchemy models
|- schemas.py          Pydantic schemas
|- database.py         Database configuration
|- deps.py             Database dependencies
|- auth.py             JWT authentication logic
|- requirements.txt    Project dependencies
|- README.md

---

#SETUP INSTRUCTIONS

1. Clone repository

git clone https://github.com/sukruthreddy2004/applyflow-backend.git
cd applyflow-backend

2. Create virtual environment

- python -m venv venv

##Windows:
- venv\Scripts\activate

##macOS / Linux:
- source venv/bin/activate

3. Install dependencies

- pip install -r requirements.txt

4. Configure database

Update database.py with your PostgreSQL credentials:

- DATABASE_URL = postgresql+psycopg://username:password@localhost/applyflow

5. Run server

- uvicorn main:app --reload

Server will run at:
http://127.0.0.1:8000

---

##API DOCUMENTATION

Swagger UI:
http://127.0.0.1:8000/docs

---

#AUTHENTICATION FLOW

1. Register user using /users/register
2. Login using /users/login
3. Receive JWT token
4. Send token in headers for protected routes

Authorization: Bearer <token>

---

#API ENDPOINTS

##USERS
POST /users/register
POST /users/login

##APPLICATIONS
POST /applications
GET /applications
PATCH /applications/{application_id}

##STATUS HISTORY
GET /applications/{application_id}/history

---

#PURPOSE

ApplyFlow demonstrates real backend engineering skills:
- Secure authentication
- Clean API design
- Relational data modeling
- Status history tracking
- Production architecture


---

#FUTURE IMPROVEMENTS

- Email notifications
- Docker support
- Cloud deployment

---

#AUTHOR

Sai Sukruth Reddy
Backend Developer (Python, FastAPI, PostgreSQL)
GitHub: https://github.com/sukruthreddy2004

