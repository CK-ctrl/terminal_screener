import pandas as pd
import matplotlib.pyplot as plt
import requests as reqs
import re
from pprint import pprint
from time import sleep
from bs4 import BeautifulSoup

url = 'http://www.screener.in/company/'
print('Welcome to Finaments, one place to get all of the financial statements of a company.')
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

reports = ['quarters','profit-loss','balance-sheet','cash-flow','ratios','shareholding']

def getTopRatios(top_ratios):
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

def getData(section):
    data = list()
    head = section.thead
    headerlist = list()
    for item in head.find_all('th'):
        headerlist.append(item.text.strip())
    data.append(headerlist)
    table = section.tbody
    for row in table.find_all('tr'):
        sublist = list()
        for item in row.find_all('td'):
            sublist.append(item.text.strip())
        data.append(sublist)
    return data

def printData(data):
    headers = data[0]
    data = data[1:]
    df = pd.DataFrame(data, columns=headers)
    df = df.set_index('')
    print(df)

def userMenu():
    print("Choose one of the following reports:")
    for i in range(len(reports)):
        print(i+1,': ' + reports[i])
    userChoice = int(input('Select: '))
    while userChoice:
        section = soup.find('section', attrs={'id':reports[userChoice-1]})
        printData(getData(section))
        print('\nEnter 0 to exit Finaments or any Report option')
        userChoice = int(input('Select: '))
    print('Thankyou for using Finaments...')
       
userMenu()