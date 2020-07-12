from requests import get
import json
from pprint import pprint
from haversine import haversine

# declare variables for weather stations and latest weather
stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

#my coordinates
my_lat =  input("latitude > ")
my_lon =  input("longitude > ")

#fetch all weather stations
all_stations = get(stations).json()['items']

#find the closest station
def find_closest():
    smallest = 20036
    for station in all_stations:
          station_lon = station['weather_stn_long']
          station_lat = station['weather_stn_lat']
          distance = haversine(my_lon, my_lat, station_lon, station_lat)
          if distance < smallest:
                smallest = distance
                closest_station = station['weather_stn_id']
    return closest_station

closest_stn = find_closest()

#convert to string
weather =  weather + str(closest_stn)

#get data and print
my_weather = get(weather).json()['items']
pprint(my_weather)
