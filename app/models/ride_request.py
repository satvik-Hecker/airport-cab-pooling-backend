from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from app.db import Base
import datetime

class RideRequest(Base):
    __tablename__ = "ride_requests"

    id= Column(Integer, primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    pickup_lat = Column(Float)
    pickup_lng = Column(Float)
    drop_lat = Column(Float)
    drop_lng = Column(Float)

    seats_requested = Column(Integer)
    luggage_units = Column(Integer)

    status = Column(String, default="PENDING")
    
    created_at = Column(DateTime, default=datetime.datetime.utcnow)