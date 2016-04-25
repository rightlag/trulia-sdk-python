# -*- coding: utf-8 -*-


class City(object):
    def __init__(self, id, name, longitude, latitude):
        self.id = int(id)
        self.name = name
        self.longitude = float(longitude)
        self.latitude = float(latitude)

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.name)


class Location(object):
    def __init__(self, city, state, search_results_url, city_guide_url,
                 heat_map_url):
        self.city = city
        self.state = state
        self.search_results_url = search_results_url
        self.city_guide_url = city_guide_url

    def __repr__(self):
        return '<{}: {}, {}>'.format(self.__class__.__name__, self.city,
                                     self.state)


class TrafficStat(object):
    def __init__(self, date, percent_state_traffic, percent_national_traffic):
        self.date = date
        self.percent_state_traffic = float(percent_state_traffic)
        self.percent_national_traffic = float(percent_national_traffic)

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.date)


class ListingsStat(object):
    def __init__(self, week_ending_date, avg_listing_value=None):
        self.week_ending_date = week_ending_date
        if avg_listing_value is None:
            avg_listing_value = []
        else:
            avg_listing_value = [Subcategory()]
        self.avg_listing_value = avg_listing_value

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__,
                                 self.avg_listing_value)


class Subcategory(object):
    def __init__(self, type, average_listing_price, number_of_properties):
        self.type = type
        self.average_listing_price = int(average_listing_price)
        self.number_of_properties = int(number_of_properties)

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.type)
