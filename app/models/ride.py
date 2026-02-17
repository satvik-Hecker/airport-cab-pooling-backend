from sqlalchemy import Column,Integer, DateTime, String
from app.db import Base
import datetime

class Ride(Base):
    __tablename__ = "rides"

    id=Column(Integer, primary_key=True, index=True)

    max_seats=Column(Integer)
    available_seats= Column(Integer)

    max_luggage =  Column(Integer)
    available_luggage = Column(Integer)

    status = Column(String, default="SEARCHING")

    created_at = Column(DateTime, default=datetime.datetime.utcnow)