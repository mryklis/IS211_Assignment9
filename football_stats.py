from bs4 import BeautifulSoup
import urllib2
import pandas as pd


page = urllib2.urlopen('http://www.cbssports.com/nfl/stats/playersort/nfl/year-2016-season-regular-category-touchdowns')

soup = BeautifulSoup(page)

column_headers = [th.getText() for th in soup.findAll('tr', limit=3)[2].findAll('th')]

data_rows = soup.findAll('tr')[3:-1]


player_data = [[td.getText() for td in data_rows[i].findAll('td')]
                for i in range(len(data_rows))]

df = pd.DataFrame(player_data, columns=column_headers)

top = df[['Player', 'Pos', 'Team', 'TD']][0:20]
print top
