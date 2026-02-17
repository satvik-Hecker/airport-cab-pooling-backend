from pydantic import BaseModel

class CancelRideRequest(BaseModel):
    ride_id: int
    user_id: int