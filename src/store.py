class Store():

  def __init__(self, streetAddress, locality, state, postal, latitude=None, longitude=None):
    self._streetAddress = streetAddress
    self._locality = locality
    self._state = state
    self._postal = postal
    self._latitude = latitude
    self._longitude = longitude

  @property
  def streetAddress(self):
    return self._streetAddress

  @streetAddress.setter
  def streetAddress(self, value):
    self._streetAddress = value

  @property
  def locality(self):
    return self._locality

  @locality.setter
  def locality(self, value):
    self._locality = value

  @property
  def state(self):
    return self._state

  @state.setter
  def state(self, value):
    self._state = value

  @property
  def postal(self):
    return self._postal

  @postal.setter
  def postal(self, value):
    self._postal = value

  @property
  def latitude(self):
    return self._latitude

  @latitude.setter
  def latitude(self, value):
    self._latitude = value

  @property
  def longitude(self):
    return self._longitude

  @longitude.setter
  def longitude(self, value):
    self._longitude = value

  def get_full_address(self):
    return "{0}, {1}, {2} {3}".format(self.streetAddress, self.locality, self.state, self.postal)

  def __str__(self):
    return "{0}, {1}, {2} {3} || LAT: {4} LONG: {5}".format(self.streetAddress, self.locality, self.state, self.postal, self.latitude, self.longitude)
