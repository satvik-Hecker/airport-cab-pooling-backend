# Smart Airport Ride Pooling Backend — Architecture

This document describes the high-level architecture of the Smart Airport Ride Pooling backend system.

## High-Level Architecture

```mermaid
graph TD

Client["Client Apps<br/>(Web / Mobile / Swagger UI)"]

API["FastAPI Backend<br/>REST API Layer"]

Services["Service Layer<br/>• Ride Pooling<br/>• Pricing Engine<br/>• Routing & Detour Logic"]

DB["PostgreSQL Database<br/>Users, Rides, Requests, Passengers"]

Client --> API
API --> Services
Services --> DB
DB --> Services
Services --> API
API --> Client
