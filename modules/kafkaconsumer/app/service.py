from json import loads
from os import environ

import psycopg

from kafka import KafkaConsumer

TOPIC_NAME = "connections"
KAFKA_SERVER = "kafka-service:9092"

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)


def db_connect(host, database, port, username, password):
    return psycopg.connect(
        host=host,
        port=port,
        dbname=database,
        user=username,
        password=password,
    )


def insert_in_db(connection):
    with psycopg.connect(db_connect(environ["DB_HOST"], environ["DB_NAME"], environ["DB_PORT"], environ["DB_USERNAME"], environ["DB_PASSWORD"])) as con
    
        sql_statement = f"INSERT INTO location (person_id, coordinate, creation_time) VALUES ({connection['person_id']}, ST_Point({connection['latitude']}, {connection['longitude']}, {connection['creation_time']}))"
        cur = con.execute(sql_statement)

        con.commit()

def consume():
    for connection in consumer:
        message = connection.value.decode("utf-8")
        location_json = loads(message)
        insert_in_db(location_json)


if __name__ == "__main__":
    consume()