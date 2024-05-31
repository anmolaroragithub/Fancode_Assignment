class User:
    def __init__(self, user_data):
        self.id = user_data['id']
        self.name = user_data['name']
        self.latitude = float(user_data['address']['geo']['lat'])
        self.longitude = float(user_data['address']['geo']['lng'])

    def is_in_fancode_city(self, lat_min, lat_max, long_min, long_max):
        return lat_min <= self.latitude <= lat_max and long_min <= self.longitude <= long_max
