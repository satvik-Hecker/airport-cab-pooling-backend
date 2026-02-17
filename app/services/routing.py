from app.services.pricing import calculate_distance

def detour_allowed(existing_pickup, new_pickup, max_detour_km=5):
    lat1, lng1 = existing_pickup
    lat2, lng2 = new_pickup

    distance = calculate_distance(lat1, lng1, lat2, lng2)

    return distance <= max_detour_km
