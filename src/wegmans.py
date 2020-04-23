"""
Generates the CSV file containing the addresses, county, latitude, and longitude
of Acme stores in New Jersey.
"""
import os, requests, csv, time, re

from store import Store
from bs4 import BeautifulSoup
from geopy import ArcGIS
from dotenv import load_dotenv

output_path = '../output/wegmans.csv'

def process():

  stores = []
  stores.append(Store("724 Route 202 South", "Bridgewater", "NJ", "08807"))
  stores.append(Store("2100 Route 70 West", "Cherry Hill", "NJ", "08002"))
  stores.append(Store("34 Sylvan Way", "Hanover", "NJ", "07054"))
  stores.append(Store("55 US Highway 9", "Englishtown", "NJ", "07726"))
  stores.append(Store("100 Farm View", "Montvale", "NJ", "07645"))
  stores.append(Store("2 Centerton Road", "Mt. Laurel", "NJ", "08054"))
  stores.append(Store("1104 Highway 35 S", "Ocean", "NJ", "07712"))
  stores.append(Store("240 Nassau Park Blvd", "Princeton", "NJ", "08540"))
  stores.append(Store("15 Woodbridge Center Drive", " Woodbridge", "New Jersey", "07095"))


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
  with open(output_path, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    for store in stores:
      writer.writerow([store.latitude, store.longitude, store.streetAddress, store.locality, store.state, store.postal])

if __name__ == '__main__':
  process()
    
