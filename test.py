import math
def distance(location1, location2):
    lat1, lon1 = location1
    lat2, lon2 = location2
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    return d

Location1= (13.1143, 80.1548)
Location2= (13.0368, 80.2676)


dist=distance(Location1,Location2)
def test_distance():
    assert int(dist)==14