# Smart Airport Ride Pooling Backend — API Documentation

This document describes all available REST APIs for the Smart Airport Ride Pooling Backend.  
The backend is built using FastAPI and provides automatic interactive documentation.
---
## Swagger Documentation

Interactive API documentation is available via Swagger UI:
http://127.0.0.1:8000/docs

Swagger allows testing APIs directly from the browser.
---
## Base Server URL
http://127.0.0.1:8000

---

## API Overview
The backend exposes the following APIs:
| API | Method | Description |
|-----|--------|-------------|
| `/users` | POST | Create new passenger |
| `/ride-request` | POST | Request pooled ride |
| `/cancel-ride` | POST | Cancel passenger ride |

---

## 1. Create User
Creates a new passenger profile.

### Endpoint
POST /users

### Request Example
json
{
  "name": "John Doe",
  "phone": "9999999999"
}

### Respone Example
{
  "id": 1,
  "name": "John Doe",
  "phone": "9999999999"
}
## 2. Create Ride Request
Requests a pooled airport ride.

### Endpoint
POST /ride-request

### Request Example
json
{
  "user_id": 1,
  "pickup_lat": 19.076,
  "pickup_lng": 72.877,
  "drop_lat": 19.0896,
  "drop_lng": 72.8656,
  "seats_requested": 1,
  "luggage_units": 0
}


### Respone Example
{
  "ride_id": 3
}
## 3. Cancel Ride
Cancels passenger participation in ride.

### Endpoint
POST /cancel-ride

### Request Example
json
{
  "ride_id": 3,
  "user_id": 1
}

### Respone Example
{
  "message": "Ride cancelled successfully"
}

## Ride Assignment Logic

Ride assignment ensures:

- Seat capacity validation
- Luggage capacity validation
- Detour tolerance enforcement
- Concurrency-safe assignment
- Dynamic ride creation

---

## Pricing Logic

Fare calculation:
Fare = (Base Fare + Distance Cost)
× Surge Multiplier
− Pooling Discount


Factors considered:

- Distance
- Passenger count
- Demand surge
- Pooling discount

---

## Concurrency Handling

Concurrency safety is implemented using:
SELECT ... FOR UPDATE

This prevents:

- Double seat booking
- Negative seat counts
- Race conditions

---

## Detour Tolerance Logic

Pooling occurs only when pickup deviation is within allowed tolerance.  
Otherwise, a new ride is created.

---

## API Testing Guide

1. Start backend:
bash
python -m uvicorn app.main:app --reload

2. Open Swagger:
http://127.0.0.1:8000/docs

3. Execute APIs interactively.

## Notes

Tables auto-create on startup.

Backend supports concurrent ride requests.

Pricing and pooling occur automatically.


