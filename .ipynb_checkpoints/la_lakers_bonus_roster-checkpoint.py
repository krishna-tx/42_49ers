from requests import get
from bs4 import BeautifulSoup
import csv

url  = "http://www.nba.com/teams/lakers/"
response = get(url)
nba = BeautifulSoup(response.content, 'html.parser')

nba_main = nba.find(class_="nba-player-index")
players = nba_main.find_all("section", attrs={"class": "nba-player-index__trending-item"})
print(len(players))
for i in range(len(players)):
    # player_name = nba.find_all("p", attrs={"class": "nba-player-index__name"})
    player_name = nba.find(class_="nba-player-index__name").text
    print(player_name)

player_details = nba.find(class_="nba-player-index__details").text.split("|")
# player_details = nba.find_all("div", attrs={"class": "nba-player-index__details"})
weight = player_details[1]
print(player_details[0])
print(weight) 