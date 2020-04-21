import requests, geopy, random
from bs4 import BeautifulSoup

shoprite_file = 'shoprite_data.html'

UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1", 
       "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )

ua = UAS[random.randrange(len(UAS))]
headers = {'user-agent': ua}

"""
Return a Response object from the passed in URL.
"""
def get_request(url):
  return requests.get(url, headers)

"""
Get a Response object from the passed in URL and return a BeautifulSoup object.
"""
def get_soup(url):
  return BeautifulSoup(get_request(url).text, 'html.parser')

def get_shoprite_data():
  with open(shoprite_file) as file:
    soup = BeautifulSoup(file.read(), 'html.parser')


get_shoprite_data();