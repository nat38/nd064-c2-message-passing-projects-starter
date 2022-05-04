import grpc
import connection_pb2
import connection_pb2_grpc

print("Sending sample payload..")

channel = grpc.insecure_channel("localhost:50056")
stub = connection_pb2_grpc.ConnectionServiceStub(channel)

connection = connection_pb2.ConnectionMessage(
    id=100,
    person_id=1,
    coordinate="0101000000842FA75F7D874140CEEEDAEF9AA45AC0",
    creation_time="2022-08-15 10:37:06.000000"
)

responce = stub.Create(connection)