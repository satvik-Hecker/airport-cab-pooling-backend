from sqlalchemy.orm import Session
from app.models.ride import Ride
from app.models.ride_passenger import RidePassenger
from app.services.pricing import calculate_price


def assign_ride(db: Session, request):

    ride = (
        db.query(Ride)
        .filter(Ride.status == "SEARCHING")
        .filter(Ride.available_seats >= request.seats_requested)
        .filter(Ride.available_luggage >= request.luggage_units)
        .with_for_update()
        .first()
    )

    if not ride:
        ride = Ride(
            max_seats=4,
            available_seats=4,
            max_luggage=4,
            available_luggage=4,
            status="SEARCHING"
        )
        db.add(ride)
        db.flush()

    ride.available_seats -= request.seats_requested
    ride.available_luggage -= request.luggage_units

    if ride.available_seats == 0:
        ride.status = "FULL"

    current_passengers = (
        db.query(RidePassenger)
        .filter(RidePassenger.ride_id == ride.id)
        .count()
    )

    total_passengers = current_passengers + 1

    fare = calculate_price(request, total_passengers)

    passenger = RidePassenger(
        ride_id=ride.id,
        user_id=request.user_id,
        pickup_order=0,
        drop_order=0,
        fare=fare
    )

    db.add(passenger)
    db.commit()
    db.refresh(ride)

    return ride
