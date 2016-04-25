from models import City
from models import ListingsStat
from models import Location
from models import Subcategory
from models import TrafficStat


class LocationInfoResponse(object):
    def __init__(self, state, cities=None):
        self.state = state
        if cities is None:
            cities = []
        else:
            cities = [
                City(*[child.text for child in city.getchildren()])
                for city in cities
            ]
        self.cities = cities

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.state)


class TruliaStatsResponse(object):
    def __init__(self, location, traffic_stats=None, listing_stats=None):
        self.location = Location(
            *[child.text for child in location.getchildren()]
        )
        if traffic_stats is None:
            traffic_stats = []
        else:
            try:
                traffic_stats = [
                    TrafficStat(
                        *[child.text for child in traffic.getchildren()]
                    )
                    for traffic in traffic_stats
                ]
            except TypeError:
                traffic_stats = []
        if listing_stats is None:
            listing_stats = []
        else:
            try:
                listing_stats = [
                    ListingsStat(
                        *[child.text for child in listing.getchildren()]
                    )
                    for listing in listing_stats
                ]
            except TypeError:
                listing_stats = []
        self.traffic_stats = traffic_stats
        self.listing_stats = listing_stats
