import imp
import phonenumbers
import folium
number="+917015203165"

from phonenumbers import geocoder

key="7480dbce3df64c238f40b5ba13bcf435"

sanNumber= phonenumbers.parse(number)

yourLocation=geocoder.description_for_number(sanNumber,'en')
print(yourLocation)

# service provider
from phonenumbers import carrier

service_provider= phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode

geocoder=OpenCageGeocode(key)

query=str(yourLocation)

result=geocoder.geocode(query)
print(result)

lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
 
print(lat,lng) 


myMap=folium,Map(lacation=[lat,lng],zoon_start=9)

folium.Marker([lat,lng],popup= yourLocation).add_to((myMap))

