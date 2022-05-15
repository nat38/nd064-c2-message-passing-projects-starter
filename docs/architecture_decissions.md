

Location Service Part of API is "carved out" cause:
- not used in ui and therefore no changes needed for current known consumers.
- high load on creating new connections expected - also using grpc to keep the data footprint low compared to REST
- 