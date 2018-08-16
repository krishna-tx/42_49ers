from ohmysportsfeedspy import MySportsFeeds
import json
import pprint

Data_query = MySportsFeeds('1.2', verbose=True)
Data_query.authenticate('7af68037-2f3f-4bf5-bbd5-173ad2', 'Dk30RQHT')

Output = Data_query.msf_get_data(league='nfl', season='upcoming', feed='active_players', team=['SF'], format='json')

states = {}

for i in range(108):
    for key, value in Output["activeplayers"]["playerentry"][i]["player"].items():
        if key == "BirthCity":
            cities = value.split(",")
            if len(cities) == 2:
                city = cities[0]
                state = cities[1]
            else:
                city = cities[0]
                state = ""
            if state not in states.keys():
                states[state] = {}
            states[state][city] = {}
#         states[state][city] = player["FirstName"] + ' ' + player["LastName"]
    
print(json.dumps(states, indent=4))