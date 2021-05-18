import pandas as pd
import matplotlib.pyplot as plt
import requests as reqs
import re
from pprint import pprint
from time import sleep
from bs4 import BeautifulSoup

url = 'http://www.screener.in/company/'
stock = input('Enter stock token: ')
r = reqs.get(url+stock)
# print(r.status_code,r.encoding)
# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
soup = BeautifulSoup(r.content,'html.parser')

content = soup.find('div', attrs={'class':'company-profile'})
about = content.find('div', attrs={'class':['sub','show-more-box','highlight']})
keypoints = content.find('div', attrs={'id':'commentary'})
top_ratios = soup.find('ul', attrs={'id':'top-ratios'})

TopRatios = dict()

for item in top_ratios.find_all('li', attrs={'class':'flex flex-space-between'}):
    key = item.find('span', attrs={'class':'name'}).text.strip()
    value = ''
    if key == 'High / Low':
        for i in item.find_all('span', attrs={'class':'number'}):
            value = value + i.text + '/'
        value = value.rstrip('/')
    else:
        value = item.find('span', attrs={'class':'number'}).text
    TopRatios[key] = value
print('Top Ratios are:')
pprint(TopRatios)

