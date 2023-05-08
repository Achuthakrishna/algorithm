#import folium
import math

# Define the locations with their latitude and longitude
locations = {
    'Ambattur': (13.1143, 80.1548),
    'Annanagar': (13.0850, 80.2101),
    'Besant Nagar': (13.0003, 80.2667),
    'Nungambakkam': (13.0569, 80.2425),
    'Velachery': (12.9815, 80.2180),
    'Avadi': (13.1067,80.0970),
    'Saidapet': (13.0213, 80.2231),
    'T.Nagar': (13.0418, 80.2341),
    'Mylapore': (13.0368, 80.2676),
    'washermanpet':(13.1148,80.2872),
    'perambur':(13.1210,80.2326),
    'sholinganallur':(12.9010, 80.2279),
    'pallikarani':(	12.941656,80.2063269),
    'Nanganallur':(12.9807,80.1882),
    'Crescent':(13.0473,80.0945)
}

# Define a function to calculate the distance between two locations
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

# Define a function to find the nearest neighbour of a location
def nearest_neighbour(location, unvisited):
    nearest = None
    min_dist = float('inf')
    for neighbour in unvisited:
        dist = distance(location, locations[neighbour])
        if dist < min_dist:
            nearest = neighbour
            min_dist = dist
    return nearest

# Define the start location
start = 'Poonamallee'

# Create a folium map with the start location
m = folium.Map(location=locations[start], zoom_start=12)

# Create a list to keep track of the order in which locations are visited
visited = [start]

# Create a list of unvisited locations
unvisited = list(locations.keys())
unvisited.remove(start)

# Find the nearest neighbour of each location until all locations are visited
while unvisited:
    current = visited[-1]
    nearest = nearest_neighbour(locations[current], unvisited)
    visited.append(nearest)
    unvisited.remove(nearest)

# Create a list of coordinates in the order in which the locations are visited
coordinates = [locations[location] for location in visited]

# Add markers to the map for each location in the order in which they are visited
for i, coordinate in enumerate(coordinates):
    folium.Marker(coordinate, popup=visited[i]).add_to(m)

# Add a line to the map connecting the locations in the order in which they are visited
folium.PolyLine(coordinates).add_to(m)

# Save the map to an HTML file
m.save('cable_fault_detection_map.html')
