from math import radians, sin, cos, asin, sqrt


class City:

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long


class DistanceCalculator:

    radius_of_earth_in_kms = 6371

    def calculate(self, city1, city2):

        # Convert cordinates from degrees to radians
        lat1 = radians(city1.lat)
        long1 = radians(city1.long)
        lat2 = radians(city2.lat)
        long2 = radians(city2.long)

        # Applying the Haversine formula
        latitude_diff = lat2 - lat1
        longitude_diff = long2 - long1

        x = sin(latitude_diff / 2)**2 + cos(lat1) * cos(lat2) * sin(longitude_diff / 2)**2
        distance_in_miles = 2 * asin(sqrt(x))

        distance_in_kms = distance_in_miles * DistanceCalculator.radius_of_earth_in_kms

        return distance_in_kms


if __name__ == "__main__":
    city1_latitude = float(input("Enter the latitude of city1: "))
    city1_longitude = float(input("Enter the longitude of city1: "))
    city2_latitude = float(input("Enter the latitude of city2: "))
    city2_longitude = float(input("Enter the longitude of city2: "))

    city1 = City(city1_latitude, city1_longitude)
    city2 = City(city2_latitude, city2_longitude)

    distance_calculator = DistanceCalculator()
    distance = distance_calculator.calculate(city1, city2)

    print(f"""City1 and City2 are {distance} kms apart.""")