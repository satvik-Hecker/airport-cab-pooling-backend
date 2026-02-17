# Low-Level Design — Backend Components

## Component Interaction

```mermaid
graph TD

API["FastAPI Routes<br/>main.py"]

RidePool["Ride Pool Service"]
Pricing["Pricing Service"]
Routing["Routing Service"]

UserModel["User Model"]
RideModel["Ride Model"]
RequestModel["RideRequest Model"]
PassengerModel["RidePassenger Model"]

DB["PostgreSQL Database"]

API --> RidePool
API --> Pricing
API --> Routing

RidePool --> RideModel
RidePool --> PassengerModel
RidePool --> RequestModel

Pricing --> RequestModel

Routing --> RequestModel

RideModel --> DB
PassengerModel --> DB
RequestModel --> DB
UserModel --> DB
