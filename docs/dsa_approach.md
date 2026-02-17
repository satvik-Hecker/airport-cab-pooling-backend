# DSA Approach and Complexity Analysis

This document explains the algorithmic approach used in the Smart Airport Ride Pooling backend.

---

## Ride Assignment Problem

The system must:

- Group passengers into shared rides.
- Respect seat and luggage constraints.
- Avoid excessive travel deviation.
- Assign rides efficiently under concurrency.

---

## Core Algorithm

When a ride request is received:

1. Search for rides in `SEARCHING` state.
2. Filter rides by available seats and luggage capacity.
3. Apply detour tolerance checks.
4. Lock selected ride row to prevent race conditions.
5. Assign passenger to ride.
6. Update ride capacity.
7. Create new ride if no match is found.

---

## Data Structures Used

- Database tables act as indexed lookup structures.
- Ride assignment uses filtered search queries.
- Passenger mapping uses relational joins.

---

## Time Complexity

### Ride Search
Searching for available rides: O(N)
Where N = number of active rides.
With database indexing:O(log N)

---

### Passenger Assignment
Updating ride capacity and inserting passenger:O(1)

---

### Overall Request Complexity: 
O(log N) with indexing
---

## Space Complexity

Space complexity grows linearly with stored rides and passengers:O(R + P)

Where:
- R = number of rides
- P = number of passengers

---

## Optimization Notes

Future improvements could include:

- Geospatial indexing
- Priority ride selection
- Route optimization engines


