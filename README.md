[![Build Status](https://travis-ci.org/rightlag/trulia-sdk-python.svg?branch=master)](https://travis-ci.org/rightlag/trulia-sdk-python)

A Python SDK to interface with the [Trulia HTTP/2 API](http://developer.trulia.com/docs/read/Home)

# Quickstart

```python
from trulia import build


def main():
    service = build('TruliaStats', '<YOUR_TRULIA_API_KEY>')
    res = service.get_city_stats(city='New York', state='NY')
    print res.location
    for traffic_stat in res.traffic_stats:
        print traffic_stat.percent_state_traffic

if __name__ == '__main__':
    main()
```

# Libraries

### `TruliaStats`

| Method                             | Description                                                          | Documentation                                                                  |
|------------------------------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------|
| `get_city_stats(**kwargs)`         | Retrieves all statistics for a city within the given date range.     | [View](http://developer.trulia.com/docs/read/TruliaStats/getCityStats)         |
| `get_county_stats(**kwargs)`       | Retrieves all statistics for a county within the given date range.   | [View](http://developer.trulia.com/docs/read/TruliaStats/getCountyStats)       |
| `get_neighborhood_stats(**kwargs)` | Retrieves all statistics for a county within the given date range.   | [View](http://developer.trulia.com/docs/read/TruliaStats/getNeighborhoodStats) |
| `get_state_stats(**kwargs)`        | Retrieves all statistics for a state within the given date range.    | [View](http://developer.trulia.com/docs/read/TruliaStats/getStateStats)        |
| `get_zip_code_stats(**kwargs)`     | Retrieves all statistics for a ZIP code within the given date range. | [View](http://developer.trulia.com/docs/read/TruliaStats/getZipCodeStats)      |

### `LocationInfo`

| Method                                | Description                                                                                                     | Documentation                                                                     |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `get_cities_in_state(**kwargs)`       | Retrieves all cities in a state, as well as the longitude and latitude of the center point of each city.        | [View](http://developer.trulia.com/docs/read/LocationInfo/getCitiesInState)       |
| `get_counties_in_state(**kwargs)`     | Retrieves all counties in a state along with the longitude and latitude of the center point of each county.     | [View](http://developer.trulia.com/docs/read/LocationInfo/getCountiesInState)     |
| `get_neighborhoods_in_city(**kwargs)` | Retrieves all Neighborhoods in a city.                                                                          | [View](http://developer.trulia.com/docs/read/LocationInfo/getNeighborhoodsInCity) |
| `get_states(**kwargs)`                | Retrieves all 50 states, along with the longitude and latitude of the center point of each state.               | [View](http://developer.trulia.com/docs/read/LocationInfo/getStates)              |
| `get_zip_codes_in_state(**kwargs)`    | Retrieves all ZIP codes in a state, as well as the longitude and latitude of the center point of each ZIP code. | [View](http://developer.trulia.com/docs/read/LocationInfo/getZipCodesInState)     |
