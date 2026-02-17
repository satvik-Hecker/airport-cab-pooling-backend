import math


def calculate_distance(lat1, lng1, lat2, lng2):
    """Approximate distance in km between two coordinates."""
    return math.sqrt((lat1 - lat2) ** 2 + (lng1 - lng2) ** 2) * 111


def calculate_price(request, passenger_count):
    """Calculate pooled ride fare."""

    BASE_FARE = 50
    PER_KM_RATE = 10

    distance = calculate_distance(
        request.pickup_lat,
        request.pickup_lng,
        request.drop_lat,
        request.drop_lng
    )

    # base price calculation
    fare = BASE_FARE + distance * PER_KM_RATE

    # surge pricing
    surge_multiplier = 1.0
    if passenger_count > 3:
        surge_multiplier = 1.2

    fare *= surge_multiplier

    # pooling discount (max 30%)
    discount = min(0.1 * passenger_count, 0.3)
    fare *= (1 - discount)

    # safety guard: price should not go below base fare
    fare = max(fare, BASE_FARE)

    return round(fare, 2)
