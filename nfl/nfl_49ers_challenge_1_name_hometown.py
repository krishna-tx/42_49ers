from ohmysportsfeedspy import MySportsFeeds

import json
import pprint

Data_query = MySportsFeeds('1.2', verbose=True)

Data_query.authenticate('7af68037-2f3f-4bf5-bbd5-173ad2', 'Dk30RQHT')

Output = Data_query.msf_get_data(league='nfl', season='upcoming', feed='active_players', team=['HOU'], format='json')

for item in Output['activeplayers']['playerentry']:
    first_name = item["player"]["FirstName"]
    last_name = item["player"]["LastName"]

    if "BirthCity" in item["player"].keys():
        hometown = item["player"]["BirthCity"]
        comma = ','
        print(first_name + last_name + comma + hometown, "USA")
    else:
        print(first_name + last_name)