from bs4 import BeautifulSoup
import urllib2

data = []
page = urllib2.urlopen('http://www.cbssports.com/nfl/stats/playersort/nfl/year-2016-season-regular-category-touchdowns')

soup = BeautifulSoup(page)

table = soup.find('table', attrs={'class':'data'})

table.findAll('tr', attrs={'align':'right'})

rows = table.findAll('td')
print rows

# for row in table.findAll('tr', attrs={'align':'right'}):
#     cells = row.findAll('td')
#     print cells