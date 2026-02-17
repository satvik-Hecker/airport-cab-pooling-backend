# Concurrency Handling Strategy

The backend supports concurrent ride requests safely.

---

## Problem

Multiple users may request rides simultaneously.

Without safeguards:

- Same seat could be assigned twice.
- Ride capacity could become negative.

---

## Strategy Used

The system uses PostgreSQL row-level locking.

During ride assignment: SELECT ... FOR UPDATE

is executed on the ride row.

This locks the ride until the transaction completes.

---

## Assignment Flow Under Concurrency

1. First request locks ride row.
2. Second request waits.
3. First request updates capacity.
4. Lock released.
5. Second request reads updated data.

---

## Benefits

- Prevents race conditions.
- Ensures seat counts remain correct.
- Allows safe concurrent operations.

---

## Scalability

Concurrency handling works across:

- Multiple backend instances
- Multiple worker processes
- High request loads

---

## Future Enhancements

- Distributed locking using Redis
- Queue-based ride assignment
- Event-driven architecture

