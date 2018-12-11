#!/usr/bin/env python

import requests, bs4, re
res = requests.get('http://finance.yahoo.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)

SnP = noStarchSoup.select('span[data-reactid="8"]')
Dow = noStarchSoup.select('span[data-reactid="13"]')
Nas = noStarchSoup.select('span[data-reactid="18"]')


if str(SnP[0])[66] == '-':
	print('Not a good day for the S&P 500: ' + str(SnP[0])[66:72])
elif str(SnP[0])[66] != '-':
	print('S&P 500 is up!: ' +  str(SnP[0])[68:74])

if str(Dow[0])[67] == '-':
	print('Not a good day for the Dow Jones: ' + str(Dow[0])[67:73])
elif str(Dow[0])[67] != '-':
	print('Dow Jones is up!: ' + str(Dow[0])[69:75])

if str(Nas[0])[67] == '-':
	print('Not a good day for the Nasdaq: ' + str(Nas[0])[67:73])
elif str(Dow[0])[67] != '-':
	print('Nasdaq is up!: ' + str(Nas[0])[69:75])

