"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_tap_test_class

from tap_norwaycitybikeapi.tap import TapNorwayCityBikeAPI

OSLO_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "client_identifier": "andrejakobsen-meltanotap",
    "city_name": "oslo",
}
BERGEN_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "client_identifier": "andrejakobsen-meltanotap",
    "city_name": "bergen",
}
TRONDHEIM_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "client_identifier": "andrejakobsen-meltanotap",
    "city_name": "trondheim",
}

# Run standard built-in tap tests from the SDK:
TestTapOsloCityBikeAPI = get_tap_test_class(
    tap_class=TapNorwayCityBikeAPI, config=OSLO_CONFIG
)
TestTapBergenCityBikeAPI = get_tap_test_class(
    tap_class=TapNorwayCityBikeAPI, config=BERGEN_CONFIG
)
TestTapTrondheimCityBikeAPI = get_tap_test_class(
    tap_class=TapNorwayCityBikeAPI, config=TRONDHEIM_CONFIG
)
