"""NorwayCityBikeAPI tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_norwaycitybikeapi import streams


class TapNorwayCityBikeAPI(Tap):
    """NorwayCityBikeAPI tap class."""

    name = "tap-norwaycitybikeapi"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "client_identifier",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The value should contain your company/organization name,"
            "follwed by a dash and the application's name",
        ),
        th.Property(
            "city_name",
            th.ArrayType(th.StringType),
            required=True,
            description="Name of Norwegian city having City Bikes",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
        th.Property(
            "api_url",
            th.StringType,
            default=" https://gbfs.urbansharing.com",
            description="The url for the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.NorwayCityBikeAPIStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.GroupsStream(self),
            streams.UsersStream(self),
        ]


if __name__ == "__main__":
    TapNorwayCityBikeAPI.cli()
