from os import environ
import logging

logger = logging.getLogger("udaconnect-api")
logging.basicConfig(level=logging.DEBUG)

from json import loads
from os import environ

import psycopg

from kafka import KafkaConsumer

TOPIC_NAME = "connections"
KAFKA_SERVER = environ["KAFKA_SERVICE"]+":"+environ["KAFKA_PORT"]

logger.info(f"connecting to " + KAFKA_SERVER)

consumer = KafkaConsumer("connections", bootstrap_servers="udaconnect-kafka.default.svc.cluster.local:9092")
logger.info(f"connected..")


def insert_in_db(connection_json):
    logger.info("postgresql://" + environ["DB_USERNAME"] + ":" + environ["DB_PASSWORD"] + "@" + environ["DB_HOST"] + ":" + environ["DB_PORT"] + "/" + environ["DB_NAME"])
    with psycopg.connect("postgresql://" + environ["DB_USERNAME"] + ":" + environ["DB_PASSWORD"] + "@" + environ["DB_HOST"] + ":" + environ["DB_PORT"] + "/" + environ["DB_NAME"]) as con:
        logger.info(connection_json)
        with con.cursor() as cur:
            cur.execute("INSERT INTO public.location (id, person_id, coordinate, creation_time) VALUES ((SELECT MAX(id) FROM public.location) + 1, %s, %s, %s)", (connection_json['person_id'], connection_json['coordinate'], connection_json['creation_time']))
        
            cur.execute("SELECT * FROM public.location ORDER BY id DESC")
            logger.info(cur.fetchone())

            con.commit()

def consume():
    for connection in consumer:
        message = connection.value.decode("utf-8")
        location_json = loads(message)
        logger.info(location_json)
        insert_in_db(location_json)


if __name__ == "__main__":
    consume()