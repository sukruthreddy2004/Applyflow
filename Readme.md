# ApplyFlow Backend 

ApplyFlow is a **backend system to track job applications and their status history**. It is designed to simulate a real-world hiring tracker used by candidates or recruiters to manage applications, status changes, and timelines.

This project is built with **FastAPI + PostgreSQL + SQLAlchemy** and follows clean backend practices such as proper schemas, models, history tracking, and API documentation.

---

##  Features

* Create job applications
* List all applications with optional status filtering
* Update application status (applied → interview → offer → rejected)
* Automatically track status change history
* PostgreSQL database integration
* Auto-generated Swagger API documentation
* Clean project structure (models, schemas, deps)

---

##  Real-World Use Case

This backend mimics how job seekers track applications across companies:

* Know where you applied
* Track progress over time
* Maintain a clean history of status changes

The same architecture can be extended for:

* ATS systems
* CRM pipelines
* Workflow tracking tools

---

##  Tech Used

* **Python**
* **FastAPI** : REST API framework
* **PostgreSQL** : Relational database
* **SQLAlchemy ORM** : Database models & queries
* **Pydantic** : Data validation & schemas
* **Uvicorn** : ASGI server

---

##  Project Structure

```text
applyflow-backend/
│- main.py        # API routes
│- database.py    # DB engine & session
│- models.py      # SQLAlchemy models
│- schemas.py     # Pydantic schemas
│- deps.py        # DB dependency
│- .gitignore     # Ignored files
│- README.md      # Project documentation
```

---

##  Getting Started

### 1️ Clone the Repository

```bash
git clone https://github.com/sukruthreddy2004/ApplyFlow.git
cd applyflow
```

### 2️ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg[binary] pydantic
```

### 4️ Configure Database

Update `DATABASE_URL` in `database.py`:

```python
DATABASE_URL = "postgresql+psycopg://username:password@localhost:5432/applyflow"
```

Make sure PostgreSQL is running.

---

##  Running the Server

```bash
uvicorn main:app --reload
```

Server will run at:

```text
http://127.0.0.1:8000
```

---

##  API Documentation (Swagger)

FastAPI provides built-in interactive docs:

* Swagger UI - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* OpenAPI JSON - [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

##  API Endpoints

### Health Check

```http
GET /
```

### Create Application

```http
POST /applications
```

### List Applications

```http
GET /applications?status=interview
```

### Update Application Status

```http
PATCH /applications/{application_id}
```

### Get Status History

```http
GET /applications/{application_id}/history
```

---

##  Future Improvements

* Authentication (JWT)
* Pagination & sorting
* Docker support
* Cloud deployment
* Frontend integration

---

##  Author

**Sai Sukruth Reddy**
Backend Developer (Python / FastAPI)

GitHub: [https://github.com/sukruthreddy2004](https://github.com/sukruthreddy2004)

---

##  Final Note

This project is built to demonstrate **real backend engineering skills**. It focuses on clean architecture, database integrity, and practical workflows used in production systems.
