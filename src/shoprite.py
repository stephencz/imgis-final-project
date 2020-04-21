"""
Generates the CSV file containing the addresses, county, latitude, and longitude
of Shoprite stores in New Jersey

The shoprite website is protected with Incapsula so scraping it is made
more difficult. Accordingly, I've manually downloaded the HTML file. From:
http://www.shoprite.com/pd/stores/NJ.
"""
import csv
from store import Store
from bs4 import BeautifulSoup
from geopy import ArcGIS

""" Path to the shoprite data file. """
data_path = 'data/shoprite.html'

def process():

  with open(data_path) as file:

    # Create BS4 Object from Data File
    soup = BeautifulSoup(file.read(), 'html.parser')

    # Create a list of the relevant list entries
    entries = [x for x in soup.findAll('li', {'itemtype': 'http://schema.org/GroceryStore'})]

    # Iterate over each entry to and create a Store object for it.
    stores = []
    for entry in entries:
      streetAddress = entry.find('span', {'itemprop': 'streetAddress'}).text
      locality = entry.find('span', {'itemprop': 'addressLocality'}).text
      state = entry.find('span', {'itemprop': 'addressRegion'}).text
      postal = entry.find('span', {'itemprop': 'postalCode'}).text

      stores.append(Store(streetAddress, locality, state, postal))

    for store in stores:
      print(store.get_full_address())


  
  