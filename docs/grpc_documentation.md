# GRPC Documentation

The grpc interface offers a service to add a new connection. Therefore the connection id, the person id, coordinated and the creation time need to be provided. This than gets pushed to a kafka topic (see also architecture diagram).

The grpc proto file looks like following:

```yaml
syntax = "proto3";

message ConnectionMessage {
  int32 id = 1;
  int32 person_id = 2;
  string coordinate = 3;
  string creation_time = 4;
}

service ConnectionService {
    rpc Create(ConnectionMessage) returns (ConnectionMessage);
}
```

One can use the api with this sample python code:

```python
import grpc
import connection_pb2
import connection_pb2_grpc

print("Sending sample payload..")

channel = grpc.insecure_channel("localhost:30002")
stub = connection_pb2_grpc.ConnectionServiceStub(channel)

#Example connection message
connection = connection_pb2.ConnectionMessage(
    id=100,
    person_id=1,
    coordinate="0101000000842FA75F7D874140CEEEDAEF9AA45AC0",
    creation_time="2022-08-15 10:37:06.000000"
)

responce = stub.Create(connection)
```

