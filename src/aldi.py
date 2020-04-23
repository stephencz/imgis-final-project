import os, csv, googlemaps, time

import pprint
from google import *
from store import Store
from geopy import ArcGIS
from dotenv import load_dotenv

""" Path to the shoprite csv file. """
output_path = '../output/aldi.csv'

def process():

  # Load enviroment variables from .env file
  load_dotenv(verbose=True)

  stores = []

  api_key = os.getenv("PLACES_API_KEY")
  gmaps = googlemaps.Client(key=api_key)

  text_search_results = googlemaps.places.places_autocomplete(gmaps, "Aldi in New Jersey")
  pprint.pprint(text_search_results)

  # Connect to ArcGIS 
  username = os.getenv('ARCGIS_USERNAME')
  password = os.getenv('ARCGIS_PASSWORD')
  referer = os.getenv('ARCGIS_REFERER')
  arcgis = ArcGIS(username, password, referer)

  # Retrieve the latitude and longitude for each store
  for store in stores:
    result = arcgis.geocode(store.get_full_address())
    store.longitude = result.longitude
    store.latitude = result.latitude
    time.sleep(0.1)

  # Create a CSV file
  with open(output_path, 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    for store in stores:
      writer.writerow([store.latitude, store.longitude, store.streetAddress, store.locality, store.state, store.postal])

if __name__ == '__main__':
  process()
    
  
  