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


plotly.tools.set_credentials_file(username='krishnar', api_key='lt8fyOo9cYYrn4BUKyQ6')
player_lat_long = pd.read_csv('la_lakers_colleges.csv')

data = [dict(
    type = 'scattergeo',
    locationmode = 'USA-states',
    lon = player_lat_long['Longitude'],
    lat = player_lat_long['Latitude'],
    text = player_lat_long['Player'] + ' ',
    mode = 'markers',
    marker = dict(
        color = "rgb(95, 250, 2)"
    )
    )]

layout = dict(
    title = 'Lakers_college',
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
py.plot(fig, validate=False, filename='la_lakers_colleges.csv')