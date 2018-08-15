from geopy.geocoders import Yandex #works
import certifi
import ssl
import geopy.geocoders
import csv
import plotly.plotly as py
import plotly
import pandas as pd

ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx


plotly.tools.set_credentials_file(username='krishnar', api_key='aP9JtUuuVf19iF1GBbMZ')
player_lat_long = pd.read_csv('player_file.csv')
player_lat_long_home = pd.read_csv('player_hometown.csv')

data = [dict(
    type = 'scattergeo',
    locationmode = 'USA-states',
    lon = player_lat_long['Longitude'],
    lat = player_lat_long['Latitude'],
    text = player_lat_long['Player'] + ' ',
    mode = 'markers',
    marker = dict(
        color = "rgb(100, 25, 25)"
    )
    )]

data_home = [dict(
    type = 'scattergeo',
    locationmode = 'USA-states',
    lon = player_lat_long_home['Longitude'],
    lat = player_lat_long_home['Latitude'],
    text = player_lat_long_home['Player'] + ' ',
    mode = 'markers',
    marker = dict(
        color = "rgb(0, 205, 250)"
    )
    )]


layout = dict(
    title = '49ers_college',
    geo = dict(
        scope='usa',
        projection=dict(type='albers usa'),
        showland = True,
        landcolor = "rgb(255, 255, 255)",
        subunitcolor = "rgb(0, 217, 217)",
        countrywidth = 0.5,
        subunitwidth = 0.5
    )
)

layout_home = dict(
    title = '49ers_hometown',
    geo = dict(
        scope='usa',
        projection=dict(type='albers usa'),
        showland = True,
        landcolor = "rgb(255, 255, 255)",
        subunitcolor = "rgb(0, 217, 217)",
        countrywidth = 0.5,
        subunitwidth = 0.5
    )
)

fig = dict(data=data, layout=layout)
py.plot(fig, validate=False, filename='player_file.csv')
fig_home = dict(data=data_home, layout=layout_home)
py.plot(fig_home, validate=False, filename='player_hometown.csv')