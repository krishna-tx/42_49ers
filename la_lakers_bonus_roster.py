from requests import get
from bs4 import BeautifulSoup
import csv

url  = "http://www.nba.com/teams/lakers/"
response = get(url)
nba = BeautifulSoup(response.content, 'html.parser')

nba_main = nba.find(class_="nba-player-index")
players = nba_main.find_all("section", attrs={"class": "nba-player-index__trending-item"})

player_detail_tags = nba.find_all("div", attrs={"class" : "nba-player-index__details"})
wt_total = 0
ht_total = 0

player_name_tags = nba.find_all("p", attrs={"class": "nba-player-index__name"})
with open('la_lakers_names.csv', 'w') as csv_file:
    for player_name_tag in player_name_tags:
        br_tag = player_name_tag.find("br")
        if br_tag is not None:
            first_name = br_tag.previous
            last_name = br_tag.next
            writer = csv.writer(csv_file)
            writer.writerow([first_name, last_name])
            
for player_detail_tag in player_detail_tags:
    details = player_detail_tag.find_all("span")
    pos = details[0].text
    ht_wt = details[1].text
    ht, wt = ht_wt.split("|")
    wt_lbs = wt.split("lbs")[0].strip()
    if wt_lbs:
        wt_total = wt_total + int(wt_lbs)

    ft, inch = ht.split("ft")
    ft = ft.strip()
    inch = inch.strip()
    if ft is not None and ft != "-":
        inch = inch.split("in")[0]

        ft_inch = int(ft)*12
        sum = int(ft_inch)+int(inch)
        ht_total = ht_total + sum
ht_avg_in = ht_total/(len(players)-1)
print("Height average-in:", round(ht_avg_in), "in")

avg_ft = int(ht_avg_in/12)
avg_in = (ht_avg_in/12-int(ht_avg_in/12))*15
# ht_avg_ft = ht_avg_in/12
print("Height average-ft:", avg_ft, "ft", int(avg_in), "in")

wt_avg = wt_total/len(players)
print("Weight average:", wt_avg, "lbs") 