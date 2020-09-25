import requests
import json
from math import *

def getISSLongitude(issData):
    issLongitude = float(issData['iss_position']['longitude'])
    
    return issLongitude
    

def getISSLatitude(issData):
    issLatitude = float(issData['iss_position']['latitude'])

    return issLatitude


    

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3956 # Radius of earth in miles. Use 6371 for km
    return c * r

def distToIss(userLat, userLon):
    i = 0
    while(i < 100):
        r = requests.get(url="http://api.open-notify.org/iss-now.json")
        issData = r.json()
        
        issLat = getISSLatitude(issData)
        issLon = getISSLongitude(issData)


        distance = haversine(userLat, userLon, issLat, issLon)
        print(distance)
        i += 1
        


def main():

    
    userLat = float(input("Enter Latitude: "))
    userLon = float(input("Enter Longitude: "))

    
    distToIss(userLat, userLon)
    

main()


