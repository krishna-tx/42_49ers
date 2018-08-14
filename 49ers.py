from requests import get
from bs4 import BeautifulSoup
import csv

url  = "https://www.49ers.com/team/players-roster/"

response = get(url)

nfl = BeautifulSoup(response.content, 'html.parser')

#print(nfl.prettify()

'''print(nfl.a)
print(nfl.p)

nfl_body = nfl.body
print(nfl_body)

print(nfl_body.a)
print(nfl_body.contents[0].next_sibling)

print(nfl_body.div)
print(nfl_body.contents[0].next_sibling.next_sibling.next_sibling)

print(nfl_body.div.header)
print(nfl_body.contents[0].next_sibling.next_sibling.next_sibling.contents[5])

print(nfl_body.div.header.div)
print(nfl_body.contents[0].next_sibling.next_sibling.next_sibling.contents[5].contents[1])

nfl_1 = nfl_body.contents[0].next_sibling.next_sibling.next_sibling
print(nfl_1)

nfl_2 = nfl_1.contents[3]
print(nfl_2)
nfl_2 = nfl_1.contents[0]
print(nfl_2)
nfl_2 = nfl_1.contents[5]
print(nfl_2)
nfl_2 = nfl_1.contents[5].next_sibling
print(nfl_2)

nfl_2 = nfl_1.contents[0]
print(nfl_2)
nfl_2 = nfl_1.contents[2]
print(nfl_2)
nfl_2 = nfl_1.contents[4]
print(nfl_2)
nfl_2 = nfl_1.contents[6]
print(nfl_2)

nfl_2 = nfl_1.contents[7]
print(nfl_2)

nfl_3 = nfl_2.contents[7]
print(nfl_3)

nfl_4 = nfl_3.div
print(nfl_4)

nfl_5 = nfl_4.div
print(nfl_5)

nfl_6 = nfl_5.div
print(nfl_6)

nfl_7 = nfl_6.div
print(nfl_7)

nfl_8 = nfl_7.div
print(nfl_8)

nfl_9 = nfl_8.div
print(nfl_9)

nfl_10 = nfl_9.contents[1]
print(nfl_10)

nfl_11 = nfl_10.contents[-2]
print(nfl_11)

nfl_12 = nfl_11.text
print(nfl_12)'''


nfl_div = nfl.find_all('div')
#print(nfl_div)

n"fl_main = nfl.find(id="main-content")
#print(nfl_main.prettify())

nfl_roster = nfl_main.find(summary="Roster")
# print("hi")

nfl_roster_body = nfl_main.find("tbody")
#print(nfl_roster_body.prettify())

# nfl_roster_body = nfl_roster.find('tbody')
#print(nfl_roster.prettify())

nfl_roster_body_tr_first = nfl_roster_body.find('tr')
#print(nfl_roster_body_tr_first.prettify())

first_name = nfl_roster_body_tr_first.find_all('td')[7].text
print(first_name)
numb = 0

# first_name = nfl_roster_body_tr_first.find_all('td')[7].text
# print(first_name)


with open('first_name.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([first_name])