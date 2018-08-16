from ohmysportsfeedspy import MySportsFeeds
import json
import pprint

Data_query = MySportsFeeds('1.2', verbose=True)
Data_query.authenticate('7af68037-2f3f-4bf5-bbd5-173ad2', 'Dk30RQHT')
Output = Data_query.msf_get_data(league='nfl', season='upcoming', feed='player_injuries', format='json')

total_weight = 0
total_height = 0

for item in Output['playerinjuries']['playerentry']:
    name = item["player"]["FirstName"] + ' ' + item["player"]["LastName"]
    weight = item["player"]["Weight"]
    height = item["player"]["Height"]
    ft, inch = height.split("'")
    
    injury = item["injury"]
    total_weight = total_weight + int(weight)
    ft_inch = int(ft)*12 + int(inch[:-1])
    total_height = total_height + ft_inch
    print(name, height, weight, injury)
avg_height = total_height/15
avg_height = avg_height/12
inch_height = avg_height-int(avg_height)
inch_height = inch_height*10
print("The average weight for an injured nfl player is:", total_weight/15, "lbs")
#inch_height = (avg_height - int(avg_height))*12
print("The average height for an injured nfl player is:", int(avg_height), "ft", round(inch_height), "inch")