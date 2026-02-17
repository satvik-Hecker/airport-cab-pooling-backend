from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db import get_db,engine,Base
from app.models import user,ride,ride_passenger,ride_request
from app.models.user import User
from app.schemas.user import UserCreate
from app.models.ride_request import RideRequest
from app.schemas.ride_request import RideRequestCreate
from app.services.ride_pool import assign_ride
from app.schemas.cancel_ride import CancelRideRequest
from app.models.ride_passenger import RidePassenger
from app.models.ride import Ride

Base.metadata.create_all(bind=engine)
app=FastAPI()

@app.get("/")
def root(db: Session = Depends(get_db)):
    return{"message":"airport backend ins running & db connected"}

@app.post("/users")
def create_user(user:UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, phone=user.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/ride-request")
def create_ride_request(
    request: RideRequestCreate,
    db: Session = Depends(get_db)
):
    ride_request= RideRequest(
        user_id=request.user_id,
        pickup_lat=request.pickup_lat,
        pickup_lng=request.pickup_lng,
        drop_lat=request.drop_lat,
        drop_lng=request.drop_lng,
        seats_requested = request.seats_requested,
        luggage_units=request.luggage_units
    )
    db.add(ride_request)
    db.commit()
    db.refresh(ride_request)
    ride = assign_ride(db,ride_request)
    ride_request.status="ASSIGNED"
    db.commit()
    return {"ride_id" : ride.id}

@app.post("/cancel-ride")
def cancel_ride(data: CancelRideRequest, db: Session = Depends(get_db)):

    passenger = db.query(RidePassenger).filter(
        RidePassenger.ride_id == data.ride_id,
        RidePassenger.user_id == data.user_id
    ).first()

    if not passenger:
        return {"error": "Passenger not found in ride"}
    
    ride = db.query(Ride).filter(
        Ride.id == data.ride_id
    ).with_for_update().first()

    ride.available_seats+=1
    ride.available_luggage+=1

    if ride.available_seats > 0:
        ride.status = "SEARCHING"
    db.delete(passenger)
    db.commit()
    return{"message": "Ride cancelled successfully"}