# Smart Airport Ride Pooling Backend

A backend system that groups airport passengers into shared rides while optimizing capacity, pricing, and route constraints.

This project was built as part of a backend engineering assignment.

---
## Features Implemented

- Passenger ride request handling
- Ride pooling based on seat and luggage capacity
- Dynamic ride creation
- Concurrency-safe ride assignment
- Real-time ride cancellation handling
- Dynamic pricing engine
- Detour tolerance enforcement
- Database persistence using PostgreSQL
- API documentation via Swagger

---
## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Uvicorn server
- Mermaid diagrams for architecture

---
## Project Structure
airport-pooling/
│
├── app/
│ ├── main.py
│ ├── db.py
│ ├── models/
│ ├── schemas/
│ └── services/
│
├── docs/
│ ├── architecture.md
│ └── low_level_design.md
│
├── requirements.txt
└── README.md


---
## Setup Instructions
### 1. Clone repository
bash
git clone https://github.com/satvik-Hecker/airport-cab-pooling-backend
cd airport-pooling

### 2. Install dependencies
bash
pip install -r requirements.txt

### 3. Setup PostgreSQL database
Create database:
sql
CREATE DATABASE airport_pooling;

### 4. Run backend server
bash
python -m uvicorn app.main:app --reload

## Server Access
Backend server runs at:
http://127.0.0.1:8000