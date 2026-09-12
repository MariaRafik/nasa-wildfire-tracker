import pandas as pd
import folium
from folium.plugins import MarkerCluster

MAP_KEY="27bbcfa151a7ba4dfbc74b5f25e07946"
source="VIIRS_NOAA20_NRT"
area="-74,-18,-44,5"
day_range=3

url=f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{MAP_KEY}/{source}/{area}/{day_range}"
df=pd.read_csv(url)
print(df.shape)
print(df.head())

m=folium.Map(location=[-8,-60], zoom_start=5,
             tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', 
             attr='Esri')
cluster=MarkerCluster().add_to(m)

for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=3,
        color='red',
        fill=True,
        fill_opacity=0.7,
    ).add_to(cluster)

m.save("wildfire_map.html")
print("Map saved as wildfire_map.html")
