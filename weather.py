from bs4 import BeautifulSoup
import urllib2


page = urllib2.urlopen('https://www.wunderground.com/history/airport/KNYC/2015/1/11/MonthlyHistory.html')

soup = BeautifulSoup(page)


dayTemp = soup.find_all('div', id='observations_details').findNext('span', 'wx-value').renderContents()

print dayTemp