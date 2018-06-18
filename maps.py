import urllib.request
import json
import os

def retornarEnd(latlng):
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + latlng + "&key=" + os.environ["mapsAPI_key"]
    r = urllib.request.urlopen(url)
    results = json.loads(r.read().decode())
    results = results['results'][0]
    end = results['formatted_address']
    maps_url = "https://www.google.com/maps/place/?q=place_id:" + results['place_id']
    return (end, maps_url)
