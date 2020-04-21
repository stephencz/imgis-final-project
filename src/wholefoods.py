import os, csv, time

from store import Store
from bs4 import BeautifulSoup
from geopy import ArcGIS
from dotenv import load_dotenv

""" Path to the shoprite data file. """
data_path = 'data/wholefoods.html'
output_path = '../output/wholefoods.csv'

def process():

  # Load enviroment variables from .env file
  load_dotenv(verbose=True)

  with open(data_path) as file:

    # Create BS4 Object from Data File
    soup = BeautifulSoup(file.read(), 'html.parser')

    # Create a list of the relevant list entries
    entries = [x for x in soup.findAll('div', {'class': 'storeAddress'})]

    # Iterate over each entry to and create a Store object for it.
    stores = []
    for entry in entries:
      data = [x for x in entry.findAll('div', {'class': 'w-store-finder-mailing-address'})]
      streetAddress = data[0].text
      locality = data[1].text.split(',')[0]
      state = data[1].text.split(',')[1].strip().split(' ')[0]
      postal = data[1].text.split(',')[1].strip().split(' ')[1] 

      stores.append(Store(streetAddress, locality, state, postal))

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
    
  
  