from os import environ
import json
import time
from concurrent import futures
from json import dumps

from kafka import KafkaProducer

import grpc
import connection_pb2
import connection_pb2_grpc

TOPIC_NAME = "connections"
KAFKA_SERVER = environ["KAFKA_SERVICE"]+":"+environ["KAFKA_PORT"]

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

class ConnectionServicer(connection_pb2_grpc.ConnectionServiceServicer):
    def Create (self, request, context):
        request_value = {
            "id" : request.id,
            "person_id" : request.person_id,
            "coordinate" : request.coordinate,
            "creation_time" : request.creation_time,
        }
        print(request_value)

        connection_json = dumps(request_value).encode()

        
        producer.send(TOPIC_NAME, connection_json)
        producer.flush()

        return connection_pb2.ConnectionMessage(**request_value)

def grpc_server():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    connection_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionServicer(), server)

    print("Server starting on port 50056...")
    server.add_insecure_port("[::]:50056")
    server.start()
    print("Server started")
    try:
        while True:
            time.sleep(100)
            print(".")
    except:
        print("error")
        server.stop(0)

if __name__ == "__main__":
    grpc_server()