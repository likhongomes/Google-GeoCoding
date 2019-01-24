import googlemaps
from datetime import datetime


print("Running the program")
gmaps = googlemaps.Client(key='AIzaSyCK7jI1dPuQBPpPnnYzWmdkYnaBWhbmyR0')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
print("Running the program")
print(geocode_result)
# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
