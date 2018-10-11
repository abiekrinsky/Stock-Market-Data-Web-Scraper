#!/usr/bin/env python

import requests, bs4
res = requests.get('http://finance.yahoo.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "lxml")

SnP = noStarchSoup.select('span[data-reactid="8"]')
Dow = noStarchSoup.select('span[data-reactid="13"]')
Nas = noStarchSoup.select('span[data-reactid="18"]')


print('S&P 500: ' + str(SnP[0])[66:72])
print('Dow Jones: ' + str(Dow[0])[67:73])
print('Nasdaq: ' + str(Nas[0])[67:73])

# Stock-Market-Data-Web-Scraper
# Stock-Market-Data-Web-Scraper
