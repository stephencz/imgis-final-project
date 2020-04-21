"""
Generates the CSV file containing the addresses, county, latitude, and longitude
of Acme stores in New Jersey.
"""
import os, requests, csv, time

from store import Store
from bs4 import BeautifulSoup
from geopy import ArcGIS
from dotenv import load_dotenv

""" Path to the shoprite data file. """
data_url = 'https://locations.traderjoes.com/nj/'
link_base = "https://locations.traderjoes.com/"
output_path = '../output/traderjoes.csv'

def get_soup(url):
  return BeautifulSoup(requests.get(url).text, 'html.parser')

def process():

  soup = get_soup(data_url)
  entries = soup.findAll('div', {'class': 'itemlist'})

  stores = []
  for entry in entries:
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

    r = requests.get(entry.find('a')['href'], headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    data = [x for x in soup.findAll('div', {'class': 'address-left'})]

    for item in data:
      spans = item.findAll('span')

      streetAddress = spans[1].text
      locality = spans[2].text
      state = spans[3].text
      postal = spans[4].text

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
    
