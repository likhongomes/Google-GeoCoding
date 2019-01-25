import requests

#Geo Coding Poject
#Likhon Gomes
#CIS 4360 Microservice Architecture

#january 25th, 2019

KEY = '3DQcCLeTMjuwtmSqX0ULLqKjtDGsROs5' #api key
LOCATION = '1208 Frankford Ave, Philadelphia, PA 19125' #input location
url = 'http://www.mapquestapi.com/geocoding/v1/address?key='+KEY+'&location='+LOCATION #making the request to get data and return a JSON file
json_data = requests.get(url).json() #parse the json data

#parse the data to get lat & lng
latitude = json_data["results"][0]["locations"][0]["latLng"]["lat"] 
longitude = json_data["results"][0]["locations"][0]["latLng"]["lng"]

#print data
print("Latitude = "+str(latitude)+"\nLongitude = "+str(longitude))





