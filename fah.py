import requests 
from bs4 import BeautifulSoup 
import datetime

#####Edit This Before Running first time######

User_name = 'YouNeedLife'
Team_id = 223518

##############################################

URL = 'https://apps.foldingathome.org/teamstats/team' + str(223518) + '.html'
req = requests.get(URL)
soup = BeautifulSoup(req.content, 'html5lib') 
tables = soup.findChildren('table')
table = tables[1]
rows = table.findChildren(['th', 'tr'])
for row in rows:
	cells = row.findChildren('td')
	for cell in cells:
		value = cell.string
		if value == User_name:
			rank = cells[0].string.strip()
			team_rank = cells[1].string.strip()
			name = cells[2].string.strip()
			credit = cells[3].string.strip()
			WUs = cells[4].string.strip()
if not name: print('Entry Not Found!')
print(str(datetime.datetime.now()), ",", rank, ",", team_rank, ",", name, ",", credit, ",", WUs)		
