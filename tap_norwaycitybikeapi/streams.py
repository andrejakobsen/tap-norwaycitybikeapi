"""Stream type classes for tap-norwaycitybikeapi."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_norwaycitybikeapi.client import NorwayCityBikeAPIStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class StationsStream(NorwayCityBikeAPIStream):
    """Define custom stream."""

    name = "stations"
    path = "/station_information.json"
    primary_keys = ["station_id"]
    # replication_key = "last_updated"
    schema = th.PropertiesList(
        th.Property(
            "station_id",
            th.StringType,
            description="The station's id",
        ),
        th.Property(
            "name",
            th.StringType,
            description="The name of the station",
        ),
        th.Property(
            "address",
            th.StringType,
            description="The address where the station is located",
        ),
        th.Property("lat", th.NumberType),
        th.Property("lon", th.NumberType),
        th.Property(
            "capacity",
            th.IntegerType,
            description="Number of bicycles that the stations can hold",
        ),
    ).to_dict()


class AvailabilityStream(NorwayCityBikeAPIStream):
    """Define custom stream."""

    name = "availability"
    path = "/station_status.json"
    primary_keys = ["station_id"]
    schema = th.PropertiesList(
        th.Property(
            "station_id",
            th.StringType,
            description="The station's id",
        ),
        th.Property(
            "is_installed",
            th.BooleanType,
            description="The name of the station",
        ),
        th.Property(
            "is_renting",
            th.BooleanType,
            description="The address where the station is located",
        ),
        th.Property("num_bikes_available", th.NumberType),
        th.Property("num_docks_available", th.NumberType),
        th.Property("last_reported", th.IntegerType),
        th.Property(
            "is_returning",
            th.BooleanType,
            description="The address where the station is located",
        ),
    ).to_dict()


class GroupsStream(NorwayCityBikeAPIStream):
    """Define custom stream."""

    name = "groups"
    path = "/groups"
    primary_keys = ["id"]
    replication_key = "modified"
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("id", th.StringType),
        th.Property("modified", th.DateTimeType),
    ).to_dict()
