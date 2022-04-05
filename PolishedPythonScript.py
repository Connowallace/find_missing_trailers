# Populate a list of all Gville reefers
def populateAllReefers():
  listAllReefers = []

  f = open("allReefers1.csv", "r")

  for x in f:
    listAllReefers.append(x.strip())
    
  f.close()

  return listAllReefers

# Populate a list of all reefers departed in last 48 hours
def populateDeparts():
  listRecentDeparts = []

  f = open("departedLast48Hours.csv", "r")

  for x in f:
    listRecentDeparts.append(x.strip())
  
  f.close()
  
  return listRecentDeparts

# Remove recent departs from complete list
def removeRecentDeparts(listAllReefers, listRecentDeparts):
  for i in listRecentDeparts:
    if i in listAllReefers:
      listAllReefers.remove(i)

  return listAllReefers

# Create a dictionary of all trailers and their location
def populateLocations():
  locations = {}

  # "Windows-1252" accounts for weird chacters in ORBCOMM loactions
  f = open("trailerLocationTest.csv", "r", encoding = "Windows-1252")

  for x in f:
    y = x.strip().split(",")
    locations[y[0]] = y[1]

  f.close()

  return locations

# Create a dictionary of trailers not on the the yard that have not departed
# in the last 48 hours
def identifyMissingTrailers(listAllReefers, locations):
  locationsNot7016 = {}
      
  for i in listAllReefers:
    if i in locations:
      if locations[i] != "Gordonsville":
        locationsNot7016[i] = locations[i]
    else:
      locationsNot7016[i] = "NO ORBCOMM DATA"

  return locationsNot7016

# Remove trailers know to be at vendors for repair from dictionary
def removeRedtags(locationsNot7016):
  f = open("redtagsAtVendors.csv", "r")

  for x in f:  
    locationsNot7016.pop(x.strip(), None)
  
  f.close()

  return locationsNot7016

# Create a CSV of all missing reefers
def createMissingTrailerList(locationsNot7016):
  f = open("missingReefers.csv", "w")

  for i in locationsNot7016:
    f.write("{},{}\n".format(i, locationsNot7016[i]))

  f.close()

# Main method
if __name__ == "__main__":
  listAllReefers = populateAllReefers()
  listRecentDeparts = populateDeparts()
  listAllReefers = removeRecentDeparts(listAllReefers, listRecentDeparts)
  locations = populateLocations()
  locationsNot7016 = identifyMissingTrailers(listAllReefers, locations)
  locationsNot7016 = removeRedtags(locationsNot7016)
  createMissingTrailerList(locationsNot7016)