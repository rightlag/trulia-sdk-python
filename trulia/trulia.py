from base import ClientConn


class LocationInfo(ClientConn):
    """LocationInfo finds geographical locations belonging to a
    particular region."""

    def __init__(self, auth):
        super(LocationInfo, self).__init__(auth)

    def get_cities_in_state(self, **kwargs):
        """Retrieves all cities in a state, as well as the longitude
        and latitude of the center point of each city."""
        fn = 'getCitiesInState'
        response = self._request(fn, **kwargs)
        return response

    def get_counties_in_state(self, **kwargs):
        """Retrieves all counties in a state along with the longitude
        and latitude of the center point of each county."""
        fn = 'getCountiesInState'
        response = self._request(fn, **kwargs)
        return response

    def get_neighborhoods_in_city(self, **kwargs):
        """Retrieves all Neighborhoods in a city."""
        fn = 'getNeighborhoodsInCity'
        response = self._request(fn, **kwargs)
        return response

    def get_states(self, **kwargs):
        """Retrieves all 50 states, along with the longitude and
        latitude of the center point of each state."""
        fn = 'getStates'
        response = self._request(fn, **kwargs)
        return response

    def get_zip_codes_in_state(self, **kwargs):
        """Retrieves all ZIP codes in a state, as well as the longitude
        and latitude of the center point of each ZIP code."""
        fn = 'getZipCodesInState'
        response = self._request(fn, **kwargs)
        return response


class TruliaStats(ClientConn):
    def __init__(self, auth):
        super(TruliaStats, self).__init__(auth)

    def get_city_stats(self, **kwargs):
        """Retrieves all statistics for a city within the given date
        range."""
        fn = 'getCityStats'
        response = self._request(fn, **kwargs)
        return response

    def get_county_stats(self, **kwargs):
        """Retrieves all statistics for a county within the given date
        range."""
        fn = 'getCountyStats'
        response = self._request(fn, **kwargs)
        return response

    def get_neighborhood_stats(self, **kwargs):
        """Retrieves all statistics for a county within the given date
        range."""
        fn = 'getNeighborhoodStats'
        response = self._request(fn, **kwargs)
        return response

    def get_state_stats(self, **kwargs):
        """Retrieves all statistics for a state within the given date
        range."""
        fn = 'getStateStats'
        response = self._request(fn, **kwargs)
        return response

    def get_zip_code_stats(self, **kwargs):
        """Retrieves all statistics for a ZIP code within the given
        date range."""
        fn = 'getZipCodeStats'
        response = self._request(fn, **kwargs)
        return response
