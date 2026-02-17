from sqlalchemy.orm import Session
from app.models.ride import Ride
from app.models.ride_passenger import RidePassenger
from app.models.ride_request import RideRequest
from app.services.pricing import calculate_price
from app.services.routing import detour_allowed


def assign_ride(db: Session, request):

    ride = (
        db.query(Ride)
        .filter(Ride.status == "SEARCHING")
        .filter(Ride.available_seats >= request.seats_requested)
        .filter(Ride.available_luggage >= request.luggage_units)
        .with_for_update()
        .first()
    )

    # --- DETOUR CHECK ---
    if ride:
        existing_passenger = (
            db.query(RidePassenger)
            .filter(RidePassenger.ride_id == ride.id)
            .first()
        )

        if existing_passenger:
            existing_request = (
                db.query(RideRequest)
                .filter(RideRequest.user_id == existing_passenger.user_id)
                .order_by(RideRequest.id.desc())
                .first()
            )

            if existing_request:
                allowed = detour_allowed(
                    (existing_request.pickup_lat,
                     existing_request.pickup_lng),
                    (request.pickup_lat,
                     request.pickup_lng)
                )

                if not allowed:
                    ride = None  # force new ride creation

    # --- CREATE NEW RIDE IF NEEDED ---
    if ride is None:
        ride = Ride(
            max_seats=4,
            available_seats=4,
            max_luggage=4,
            available_luggage=4,
            status="SEARCHING"
        )
        db.add(ride)
        db.flush()

    # --- UPDATE CAPACITY ---
    ride.available_seats -= request.seats_requested
    ride.available_luggage -= request.luggage_units

    if ride.available_seats == 0:
        ride.status = "FULL"

    # --- PRICING ---
    current_passengers = (
        db.query(RidePassenger)
        .filter(RidePassenger.ride_id == ride.id)
        .count()
    )

    total_passengers = current_passengers + 1
    fare = calculate_price(request, total_passengers)

    # --- PASSENGER MAPPING ---
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
