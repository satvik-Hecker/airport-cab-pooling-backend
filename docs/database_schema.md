# Database Schema and Indexing Strategy

The system uses PostgreSQL to store ride pooling data.

---

## Database Tables

### Users

Stores passenger information.

| Column | Description |
|--------|-------------|
| id | User identifier |
| name | Passenger name |
| phone | Contact number |

---

### Rides

Stores ride instances.

| Column | Description |
|--------|-------------|
| id | Ride identifier |
| max_seats | Total seats |
| available_seats | Remaining seats |
| max_luggage | Luggage capacity |
| available_luggage | Remaining luggage capacity |
| status | SEARCHING / FULL |

---

### Ride Requests

Stores ride requests.

| Column | Description |
|--------|-------------|
| id | Request identifier |
| user_id | Passenger ID |
| pickup_lat | Pickup latitude |
| pickup_lng | Pickup longitude |
| drop_lat | Drop latitude |
| drop_lng | Drop longitude |
| seats_requested | Seats needed |
| luggage_units | Luggage units |

---

### Ride Passengers

Maps passengers to rides.

| Column | Description |
|--------|-------------|
| id | Mapping identifier |
| ride_id | Ride reference |
| user_id | Passenger reference |
| pickup_order | Pickup sequence |
| drop_order | Drop sequence |
| fare | Passenger fare |

---

## Indexing Strategy

Indexes improve ride search performance.

Recommended indexes:

### Rides Table
- Index on `status`
- Index on `available_seats`
- Index on `available_luggage`

### Ride Passengers Table
- Index on `ride_id`

### Ride Requests Table
- Index on `user_id`

---

## Benefits of Indexing

Indexes help:

- Reduce ride search latency
- Handle high request throughput
- Maintain low response time

---

## Future Improvements

- Geospatial indexes for location queries
- Partitioning rides by region
