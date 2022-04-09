import phonenumbers
number = "+91 8059960375"

from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number,"CH")
print(geocoder. description_for_number(ch_nmber,"en"))

from phonenumbers import carrier 
service_nmber= phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_nmber,"en"))



