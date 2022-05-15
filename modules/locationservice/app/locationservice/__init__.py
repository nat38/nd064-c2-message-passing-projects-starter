from app.locationservice.models import Location  # noqa
from app.locationservice.schemas import LocationSchema  # noqa


def register_routes(api, app, root="api"):
    from app.locationservice.controllers import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
