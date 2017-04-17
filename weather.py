from bs4 import BeautifulSoup
import urllib2
import pandas as pd


page = urllib2.urlopen('https://www.wunderground.com/history/airport/KNYC/2015/1/11/MonthlyHistory.html')

soup = BeautifulSoup(page)

column_data = [th.getText() for th in soup.findAll('table', id='obsTable')[0].findAll('tbody')[0].findAll('td')]

data_rows = soup.findAll('table', id='obsTable')[0].findAll('tr')[2:]

weather_data = [[td.getText() for td in data_rows[i].findAll('td')] for i in range(len(data_rows))]

df = pd.DataFrame(weather_data, columns=column_data, index=None, dtype=int)

df2 = df.iloc[:,[0,2]]

print df2