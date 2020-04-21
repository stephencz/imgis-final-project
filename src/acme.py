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
data_url = 'https://local.acmemarkets.com/nj.html'
link_base = "https://local.acmemarkets.com/"
output_path = '../output/acme.csv'

def get_soup(url):
  return BeautifulSoup(requests.get(url).text, 'html.parser')

def process():
  soup = get_soup(data_url)

  entries = [x for x in soup.findAll('a', {'class': 'Directory-listLink'})]

  data_links = []
  for entry in entries:
      if(int(entry['data-count'][1:-1]) > 1):
        sub_soup = get_soup(link_base + str(entry['href']))
        links = [x for x in sub_soup.findAll('a', {'class': 'Teaser-titleLink'})]
        for link in links:
          data_links.append(link_base + str(link['href'])[2:])

      else:
        data_links.append(link_base + str(entry['href']))

  for link in data_links:
    print(link)

  stores = []
  for link in data_links:
    print(link)

    soup = get_soup(link)

    streetAddress = soup.find(itemprop='streetAddress').get('content')
    locality = soup.find(itemprop='addressLocality').get('content')
    state = soup.find('abbr', {'class': 'c-address-state'}).text
    postal = soup.find('span', {'class', 'c-address-postal-code'}).text

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
    
