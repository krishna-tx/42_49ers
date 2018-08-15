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

data = [dict(
    type = 'scattergeo',
    locationmode = 'USA-states',
    lon = player_lat_long['Longitude'],
    lat = player_lat_long['Latitude'],
    text = player_lat_long['Player'] + ' ',
    mode = 'markers'
    )]

layout = dict(
    title = '49ers',
    geo = dict(
        scope='usa',
        projection=dict(type='albers usa'),
        showland = True,
        landcolor = "rgb(250, 250, 250",
        subunitcolor = "rgb(217, 217, 217)",
        countrycolor = "rgb(217, 217, 217)",
        countrywidth = 0.5,
        subunitwidth = 0.5
    )
)

fig = dict(data=data, layout=layout)
py.plot(fig, validate=False, filename='player_file.csv')