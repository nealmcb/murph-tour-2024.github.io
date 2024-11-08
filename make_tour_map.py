import folium

# Reinitialize map since the environment was reset
tour_map = folium.Map(location=[36.0, -104.0], zoom_start=5)

# List of all tour stops with coordinates including the final stop
all_tour_stops = [
    {"date": "21 Nov", "location": "Boot Barn Hall, Colorado Springs, CO", "coords": [38.8339, -104.8214]},
    {"date": "22 Nov", "location": "Boot Barn Hall, Colorado Springs, CO", "coords": [38.8339, -104.8214]},
    {"date": "23 Nov", "location": "Avalon Theatre, Grand Junction, CO", "coords": [39.0639, -108.5506]},
    {"date": "24 Nov", "location": "The Lincoln Center, Fort Collins, CO", "coords": [40.5853, -105.0844]},
    {"date": "30 Nov", "location": "Kathleen C. Cailloux City Center for the Performing Arts, Kerrville, TX", "coords": [30.0474, -99.1403]},
    {"date": "01 Dec", "location": "Kathleen C. Cailloux City Center for the Performing Arts, Kerrville, TX", "coords": [30.0474, -99.1403]},
    {"date": "05 Dec", "location": "The Ector Theatre, Odessa, TX", "coords": [31.8457, -102.3676]},
    {"date": "06 Dec", "location": "Historic Shuler Theater, Raton, NM", "coords": [36.9031, -104.4394]},
    {"date": "07 Dec", "location": "Spencer Theater, Alto, NM", "coords": [33.3884, -105.6797]},
    {"date": "08 Dec", "location": "Santa Fe, NM", "coords": [35.6870, -105.9378]},
    {"date": "09 Dec", "location": "Amarillo, TX", "coords": [35.2210, -101.8313]},
    {"date": "10 Dec", "location": "Lubbock, TX", "coords": [33.5779, -101.8552]},
    {"date": "11 Dec", "location": "Lubbock, TX", "coords": [33.5779, -101.8552]},
    {"date": "12 Dec", "location": "Anson, TX", "coords": [32.7562, -99.8965]},
    {"date": "14 Dec", "location": "Enid, OK", "coords": [36.3956, -97.8784]},
    {"date": "15 Dec", "location": "McPherson, KS", "coords": [38.3708, -97.6642]},
    {"date": "16 Dec", "location": "Waco, TX", "coords": [31.5493, -97.1467]},
    {"date": "18 Dec", "location": "Corpus Christi, TX", "coords": [27.8006, -97.3964]},
    {"date": "19 Dec", "location": "Grand Prairie, TX", "coords": [32.7459, -96.9978]},
    {"date": "20 Dec", "location": "Chappell Hill, TX", "coords": [30.1402, -96.2572]},
    {"date": "22 Dec", "location": "Austin, TX", "coords": [30.2672, -97.7431]}
]

# Create list for locations to draw line
locations = []

# Add markers and line coordinates
for stop in all_tour_stops:
    locations.append(stop["coords"])
    folium.Marker(
        location=stop["coords"],
        popup=f"{stop['date']}: {stop['location']}",
        tooltip=f"{stop['date']} - {stop['location']}"
    ).add_to(tour_map)

# Draw a polyline to connect all tour stops
folium.PolyLine(locations, color="blue", weight=2.5, opacity=1).add_to(tour_map)

# Save the final map to an HTML file
tour_map.save('/mnt/data/michael_martin_murphey_final_tour_map.html')
