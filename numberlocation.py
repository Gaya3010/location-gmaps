

import phonenumbers
from phonenumbers import geocoder
import folium 
#number = "+917775961767"
number = input("enter mobile number : ")
number = "+91" +number
key = "22c0cdf5e19945b7879ed791f92e98b4"
samnumber = phonenumbers.parse(number)
yourlocation = geocoder.description_for_number(samnumber,'en')
print(yourlocation)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourlocation)

results =geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat,lng],zoom_start = 9)

folium.Marker([lat,lng],popup=yourlocation).add_to(myMap)
myMap.save("mylocation.html")
