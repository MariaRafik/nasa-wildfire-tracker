# 🌍 NASA Near-Real-Time Wildfire Tracker

An interactive data visualization project built with Python that fetches near-real-time thermal anomaly data from the [NASA FIRMS API](https://firms.modaps.eosdis.nasa.gov/) and maps active wildfires.

![Map Preview](map_preview.png)

## 🔍 Project Overview
This script connects to the VIIRS sensor on the NOAA-20 satellite to pull raw wildfire data. By default, the coordinates are set over central South America, which currently tracks approximately **10,000 active fire hotspots** over a 3-day period. The data is parsed using Pandas and visualized on an interactive web map using Folium.

## ✨ Features
* **Live Satellite Data:** Directly queries the NASA API for the latest tabular CSV thermal data.
* **Fully Customizable:** You can easily change the `area` (bounding box coordinates) and `day_range` variables in the code to track fires in any region of the world.
* **Interactive Clustering:** Utilizes `Folium MarkerCluster` to smoothly render thousands of data points without lagging the browser.

## 🚀 How to Run Locally

1. **Get an API Key:** Register for a free API key at [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/api/).
2. **Setup the Code:** Clone this repository and insert your key into the `MAP_KEY` variable inside the script.
3. **Install Dependencies:** 
   ```bash
   pip install -r requirements.txt
