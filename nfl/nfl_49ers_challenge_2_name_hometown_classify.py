from ohmysportsfeedspy import MySportsFeeds
import json
import pprint

Data_query = MySportsFeeds('1.2', verbose=True)
Data_query.authenticate('7af68037-2f3f-4bf5-bbd5-173ad2', 'Dk30RQHT')

Output = Data_query.msf_get_data(league='nfl', season='upcoming', feed='active_players', team=['SF'], format='json')

states = {}

for i in range(108):
    player_info = Output["activeplayers"]["playerentry"][i]["player"]
    print(player_info["FirstName"], player_info["LastName"])
    if "BirthCity" in player_info:
        city_state = player_info["BirthCity"]
        if "," in city_state:
            city, state = city_state.split(",")
            if state not in states: 
                states[state] = {}
            states[state][city] = player_info["FirstName"] + " " + player_info["LastName"]
    
print(json.dumps(states, indent=4))