from pathlib import Path

"""
Checks if a cache exists for the shoprite data.
@return True if the cache exists. Otherwise false.
"""
def check_for_cache(cache_path):
  cache = Path(cache_path)
  if cache.is_file():
    return True

  return False

"""
Creates a local copy of the requests file.
"""
def cache_data_source(soup, cache_path):  
  pass