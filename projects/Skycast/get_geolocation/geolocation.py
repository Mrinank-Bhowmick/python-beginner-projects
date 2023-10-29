from geopy.geocoders import Nominatim


class GeolocationModel:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="my-app")

    def get_location_by_name(self, location):
        location_data = self.geolocator.geocode(location)

        if location_data is None:
            return None

        latitude = location_data.latitude
        longitude = location_data.longitude
        return latitude, longitude
