import requests
import urllib
import xml.etree.ElementTree as ET

from responses import LocationInfoResponse
from responses import TruliaStatsResponse


class ClientConn(object):
    ADDRESS = 'http://api.trulia.com/webservices.php'

    def __init__(self, auth):
        self.auth = auth
        self.ADDRESS += '?library={}'.format(self)

    def _request(self, fn, **kwargs):
        kwargs['function'] = fn
        kwargs['apikey'] = self.auth
        params = urllib.urlencode(kwargs)
        url = self.ADDRESS + '&' + params
        response = requests.get(url)
        if response.status_code not in xrange(200, 300):
            response.raise_for_status()
        root = ET.fromstring(response.text)
        if str(self) == 'LocationInfo':
            context = root.find('response').find('LocationInfo')
            deserialized = LocationInfoResponse(
                context.find('stateCode').text,
                context.findall('city')
            )
        elif str(self) == 'TruliaStats':
            context = root.find('response').find('TruliaStats')
            deserialized = TruliaStatsResponse(
                context.find('location'),
                context.findall('trafficStats'),
                context.findall('listingStats')
            )
        return deserialized

    def __repr__(self):
        return self.__class__.__name__
