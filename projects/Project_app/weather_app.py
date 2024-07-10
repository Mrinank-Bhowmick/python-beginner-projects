# -*- coding: utf-8 -*-
"""
Streamlit Weather App
=====================

This is a basic Streamlit webapp displaying the current temperature, wind speed
and wind direction as well as the temperature and precipitation forecast for 
the week ahead at one of 40,000+ cities and towns around the globe. The weather
forecast is given in terms of the actual timezone of the city of interest.
Additionally, a map with the location of the requested city is displayed.

- The weather data is from http://open-meteo.com
- The list with over 40,000 cities around world stems from 
  https://simplemaps.com/data/world-cities

Enjoy exploring!

"""

import streamlit as st
import pandas as pd
import requests
import json
from plotly.subplots import make_subplots
import plotly.graph_objs as go
from datetime import datetime
from datetime import timezone as tmz
import pytz
from tzwhere import tzwhere
import folium
from streamlit_folium import folium_static


# Title and description for your app
st.title("How's the weather? :sun_behind_rain_cloud:")

st.subheader("Choose location")

file = "worldcities.csv"
data = pd.read_csv(file)


# Select Country
country_set = set(data.loc[:,"country"])
country = st.selectbox('Select a country', options=country_set)

country_data = data.loc[data.loc[:,"country"] == country,:]

city_set = country_data.loc[:,"city_ascii"] 

city = st.selectbox('Select a city', options=city_set)


lat = float(country_data.loc[data.loc[:,"city_ascii"] == city, "lat"])
lng = float(country_data.loc[data.loc[:,"city_ascii"] == city, "lng"])

response_current = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&current_weather=true')

st.subheader("Current weather")

result_current = json.loads(response_current._content)

current = result_current["current_weather"]
temp = current["temperature"]
speed = current["windspeed"]
direction = current["winddirection"]

# Increment added or substracted from degree values for wind direction
ddeg = 11.25

# Determine wind direction based on received degrees
if direction >= (360-ddeg) or direction < (0+ddeg):
    common_dir = "N"
elif direction >= (337.5-ddeg) and direction < (337.5+ddeg):
    common_dir = "N/NW"
elif direction >= (315-ddeg) and direction < (315+ddeg):
    common_dir = "NW"
elif direction >= (292.5-ddeg) and direction < (292.5+ddeg):
    common_dir = "W/NW"
elif direction >= (270-ddeg) and direction < (270+ddeg):
    common_dir = "W"
elif direction >= (247.5-ddeg) and direction < (247.5+ddeg):
    common_dir = "W/SW"
elif direction >= (225-ddeg) and direction < (225+ddeg):
    common_dir = "SW"
elif direction >= (202.5-ddeg) and direction < (202.5+ddeg):
    common_dir = "S/SW"
elif direction >= (180-ddeg) and direction < (180+ddeg):
    common_dir = "S"
elif direction >= (157.5-ddeg) and direction < (157.5+ddeg):
    common_dir = "S/SE"
elif direction >= (135-ddeg) and direction < (135+ddeg):
    common_dir = "SE"
elif direction >= (112.5-ddeg) and direction < (112.5+ddeg):
    common_dir = "E/SE"
elif direction >= (90-ddeg) and direction < (90+ddeg):
    common_dir = "E"
elif direction >= (67.5-ddeg) and direction < (67.5+ddeg):
    common_dir = "E/NE"
elif direction >= (45-ddeg) and direction < (45+ddeg):
    common_dir = "NE"
elif direction >= (22.5-ddeg) and direction < (22.5+ddeg):
    common_dir = "N/NE"


st.info(f"The current temperature is {temp} °C. \n The wind speed is {speed} m/s. \n The wind is coming from {common_dir}.")

st.subheader("Week ahead")

st.write('Temperature and rain forecast one week ahead & city location on the map', unsafe_allow_html=True)

with st.spinner('Loading...'):
    response_hourly = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&hourly=temperature_2m,precipitation')
    result_hourly = json.loads(response_hourly._content)
    hourly = result_hourly["hourly"]
    hourly_df = pd.DataFrame.from_dict(hourly)
    hourly_df.rename(columns = {'time':'Week ahead'}, inplace = True)
    hourly_df.rename(columns = {'temperature_2m':'Temperature °C'}, inplace = True)
    hourly_df.rename(columns = {'precipitation':'Precipitation mm'}, inplace = True)
    
    tz = tzwhere.tzwhere(forceTZ=True)
    timezone_str = tz.tzNameAt(lat, lng, forceTZ=True) # Seville coordinates
    
    timezone_loc = pytz.timezone(timezone_str)
    dt = datetime.now()
    tzoffset = timezone_loc.utcoffset(dt)#-timedelta(hours=1,minutes=0)
    
    
    # Create figure with secondary y axis
    fig = make_subplots(specs=[[{"secondary_y":True}]])
    
    
    week_ahead = pd.to_datetime(hourly_df['Week ahead'],format="%Y-%m-%dT%H:%M")
    
    # Add traces
    fig.add_trace(go.Scatter(x = week_ahead+tzoffset, 
                             y = hourly_df['Temperature °C'],
                             name = "Temperature °C"),
                  secondary_y = False,)
    
    fig.add_trace(go.Bar(x = week_ahead+tzoffset, 
                         y = hourly_df['Precipitation mm'],
                         name = "Precipitation mm"),
                  secondary_y = True,)
    
    time_now = datetime.now(tmz.utc)+tzoffset
    
    fig.add_vline(x = time_now, line_color="red", opacity=0.4)
    fig.add_annotation(x = time_now, y=max(hourly_df['Temperature °C'])+5,
                text = time_now.strftime("%d %b %y, %H:%M"),
                showarrow=False,
                yshift=0)
    
    fig.update_yaxes(range=[min(hourly_df['Temperature °C'])-10,
                            max(hourly_df['Temperature °C'])+10],
                      title_text="Temperature °C",
                     secondary_y=False,
                     showgrid=False,
                     zeroline=False)
        
    fig.update_yaxes(range=[min(hourly_df['Precipitation mm'])-2,
                            max(hourly_df['Precipitation mm'])+8], 
                      title_text="Precipitation (rain/showers/snow) mm",
                     secondary_y=True,
                     showgrid=False)
    
    
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=0.7
    ))
    
    # center on Liberty Bell, add marker
    m = folium.Map(location=[lat, lng], zoom_start=7)
    folium.Marker([lat, lng], 
              popup=city+', '+country, 
              tooltip=city+', '+country).add_to(m)
    
    # call to render Folium map in Streamlit
    
    # Make folium map responsive to adapt to smaller display size (
    # e.g., on smartphones and tablets)
    make_map_responsive= """
     <style>
     [title~="st.iframe"] { width: 100%}
     </style>
    """
    st.markdown(make_map_responsive, unsafe_allow_html=True)
    
    # Display chart
    st.plotly_chart(fig, use_container_width=True)
    
    # Display map
    st_data = folium_static(m, height = 370)
    
       
    # Concluding remarks
    st.write('Weather data source: [http://open-meteo.com](http://open-meteo.com) \n\n'+
             'List of 40,000+ world cities: [https://simplemaps.com/data/world-cities](https://simplemaps.com/data/world-cities) \n\n')
    st.write('Thanks for stopping by. Cheers!')



