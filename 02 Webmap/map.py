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

fg_vol=folium.FeatureGroup('Volcanoes')
for lat, lon, name, elev in zip(volcano_data['LAT'], volcano_data['LON'], volcano_data['NAME'], volcano_data['ELEV']):
    fg_vol.add_child(folium.CircleMarker(location = [lat, lon], popup=f"{name} @ {elev} m", fill=True, 
                                        fill_color = get_color(elev), color= 'grey', fill_opacity=0.7, radius=6))

fg_pop=folium.FeatureGroup('Population')
fg_pop.add_child(folium.GeoJson(data= (open('world.json', 'r', encoding="utf-8-sig").read()),
                             style_function= lambda x:{'fillColor':'green' if x['properties']['POP2005']<=10000000 
                             else 'orange' if 10000000<x['properties']['POP2005']<=20000000 else 'red'}))
map.add_child(fg_vol)
map.add_child(fg_pop)
map.add_child(folium.LayerControl())
map.save('map1.html')