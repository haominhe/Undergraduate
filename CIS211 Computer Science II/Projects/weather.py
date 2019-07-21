"""
CIS 211 Winter 2015
Haomin He
Extra Credit Challenge: Mashup

Write a program that reads a zip code from the command line and prints a
weather prediction for that location

First use geocoder.us to fetch the location information for the zip code
http://geocoder.us/service/json/geocode?zip=XXXXX

Extract the the latitude and longitude, pass it in a call to forecast.weather.gov
http://forecast.weather.gov/MapClick.php?lat=XX&lon=XX&FcstType=json
"""

from sys import argv
from urllib.request import *
import json
punctuation1 = '!"#$%&()* "./:;<=>?@[\]^_`{|}~'

def weather():
    zipcode = argv[1]

    site = "http://geocoder.us"
    service = "/service/json/geocode?zip="

    url = site + service + zipcode

    content = urlopen(url).read().decode()

    city0 = content.split(',')[1].strip().split(':') # a list of string
    latitude0 = content.split(',')[2].strip().split(':') 
    longitute0 = content.split(',')[3].strip().split(':')

    city = city0[1].strip(punctuation1)
    latitude = latitude0[1].strip(punctuation1)
    longitute = longitute0[1].strip(punctuation1)

    urlweather = "http://forecast.weather.gov/MapClick.php?lat={}&lon={}&FcstType=json".format(latitude, longitute)
    contentweather = urlopen(urlweather).read().decode()
    x = json.loads(contentweather)
    currentweather = x['data']['text'][0]
    currenttime = x['time']['startPeriodName'][0].lower()
    print("Forecast for {} in {}: {}".format(currenttime, city, currentweather))
    
    
   


if __name__ == "__main__":
    weather()










