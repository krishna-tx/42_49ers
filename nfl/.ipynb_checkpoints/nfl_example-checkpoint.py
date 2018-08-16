from ohmysportsfeedspy import MySportsFeeds

import json
import pprint

Data_query = MySportsFeeds('1.2', verbose=True)

Data_query.authenticate('7af68037-2f3f-4bf5-bbd5-173ad2', 'Dk30RQHT')

Output = Data_query.msf_get_data(league='nfl', season='upcoming', feed='player_injuries', format='json')
print(json.dumps(Output, indent=4))

# for item in Output['playerinjuries']['playerentry']:

#     name = item["player"]["FirstName"] + ' ' + item["player"]["LastName"]
#     print(name)