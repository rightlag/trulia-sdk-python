import logging
import os
import sys
import unittest

from trulia import build
from trulia import LocationInfo
from trulia import TruliaStats

try:
    _AUTH = os.environ['TRULIA_API_KEY']
except KeyError:
    logging.error('can\'t find `TRULIA_API_KEY` environment variable')
    sys.exit(1)


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
