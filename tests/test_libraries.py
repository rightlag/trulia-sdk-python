import os
import unittest

from trulia import build
from trulia import LocationInfo
from trulia import TruliaStats
from trulia.responses import LocationInfoResponse

_AUTH = os.environ['TRULIA_API_KEY']


class LocationInfoTestCase(unittest.TestCase):
    def setUp(self):
        self.service = build('LocationInfo', _AUTH)

    def test_library_type(self):
        self.assertTrue(isinstance(self.service, LocationInfo))


class TruliaStatsTestCase(unittest.TestCase):
    def setUp(self):
        self.service = build('TruliaStats', _AUTH)

    def test_library_type(self):
        self.assertTrue(isinstance(self.service, TruliaStats))
