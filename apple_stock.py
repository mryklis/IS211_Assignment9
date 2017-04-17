from bs4 import BeautifulSoup
import urllib2
import pandas as pd

import StringIO

page = urllib2.urlopen('http://chart.finance.yahoo.com/table.csv?s=AAPL&a=9&b=1&c=2016&d=9&e=31&f=2016&g=d&ignore=.csv')

soup = BeautifulSoup(page)

data = str(soup.findAll('p'))

d = data.lstrip('[<p>').rstrip('</p>]')

df = pd.read_csv(StringIO.StringIO(d), sep=',')

df2 = df[['Date', 'Close']]
print df2



