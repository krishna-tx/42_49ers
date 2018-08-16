from ohmysportsfeedspy import MySportsFeeds
import json
import pprint

Data_query = MySportsFeeds('1.2', verbose=True)
Data_query.authenticate('afc252ab406ec30e66d849ab957c6cc6275bbda94b2032a1f6f0c8b5ca75fd2a', 'ee88662fbead382e5f4352709331284f100e24e512f45d3f73d1e151c986aaa8')

Output = Data_query.msf_get_data(league='nfl', season='upcoming', feed='active_players', team=['SF'], format='json')

# states = {}

# for i in range(108):
#     for key, value in Output["activeplayers"]["playerentry"][i]["player"].items():
#         if key == "BirthCity":
#             cities = value.split(",")
#             if len(cities) == 2:
#                 city = cities[0]
#                 state = cities[1]
#             else:
#                 city = cities[0]
#                 state = ""
#             if state not in states.keys():
#                 states[state] = {}
#             states[state][city] = {}
    
# print(json.dumps(states, indent=4))