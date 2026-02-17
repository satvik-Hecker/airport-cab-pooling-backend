from pydantic import BaseModel


class RideRequestCreate(BaseModel):
    user_id: int
    pickup_lat: float
    pickup_lng: float
    drop_lat: float
    drop_lng: float
    seats_requested: int
    luggage_units: int
