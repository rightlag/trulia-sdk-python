from trulia import LocationInfo
from trulia import TruliaStats


def build(service, auth):
    """Return a new instance of a service."""
    return {
        'LocationInfo': LocationInfo,
        'TruliaStats': TruliaStats,
    }[service](auth)
