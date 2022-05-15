import logging
from datetime import datetime

from app.locationservice.models import Location, Person
from app.locationservice.schemas import (
    PersonSchema,
    LocationSchema,
    
)
from app.locationservice.services import LocationService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("udaconnect-api")

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaLocationService", description="Retreive locaions")  # noqa


# TODO: This needs better exception handling
logger.info("Recevied get request")

@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)

        return location

