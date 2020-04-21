"""
Generates the CSV file containing the addresses, county, latitude, and longitude
of IGA stores in New Jersey.

The shoprite website is protected with Incapsula so scraping it is made
more difficult. Accordingly, I've manually downloaded the HTML file. From:
http://www.shoprite.com/pd/stores/NJ.
"""
import os, requests, csv, time

from store import Store
from bs4 import BeautifulSoup
from geopy import ArcGIS
from dotenv import load_dotenv

""" Path to the shoprite data file. """
data_url = 'https://www.iga.com/find-a-store?page={1}&locationLat=40.0583238&locationLng=-74.4056612'
pages = 185
output_path = '../output/iga.csv'

def get_soup(url):
  return BeautifulSoup(requests.get(url).text, 'html.parser')

def process():




if __name__ == '__main__':
  process()
    
