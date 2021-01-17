import folium
import pandas

def get_color(elev):
    if elev < 1000:
        return 'green'
    elif elev < 3000:
        return 'orange'
    else:
        return 'red'

volcano_data = pandas.read_csv('Volcanoes.txt')
map = folium.Map(location=[28.47104, -77.04616], zoom_start=6, tiles="Stamen Terrain")

fg=folium.FeatureGroup('My Map')
for lat, lon, name, elev in zip(volcano_data['LAT'], volcano_data['LON'], volcano_data['NAME'], volcano_data['ELEV']):
    fg.add_child(folium.CircleMarker(location = [lat, lon], popup=f"{name} @ {elev} m", fill=True, 
                                        fill_color = get_color(elev), color= 'grey', fill_opacity=0.7, radius=6))

map.add_child(fg)
map.save('map1.html')