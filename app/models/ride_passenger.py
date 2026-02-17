from sqlalchemy import Column, Integer, Float, ForeignKey
from app.db import Base

class RidePassenger(Base):
    __tablename__ = "ride_passengers"

    id=Column(Integer, primary_key=True, index=True)

    ride_id =Column(Integer,ForeignKey("rides.id"))
    user_id=Column(Integer, ForeignKey("users.id"))

    pickup_order=Column(Integer)
    drop_order=Column(Integer) 

    fare=Column(Float)