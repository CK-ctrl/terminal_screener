import pandas as pd
import matplotlib.pyplot as plt
import requests as reqs
import re
from nsetools import Nse
from pprint import pprint
from time import sleep
from bs4 import BeautifulSoup

nse = Nse()
stocks = nse.get_stock_codes()

# print("Enter a stock quote: ")
# quote = input()
# q = nse.get_quote(quote)

url = 'http://www.screener.in/company/'
# for i in stocks:
#     stockurl = url + i
#     r = reqs.get(stockurl)
#     print(i,':\t\t',r.status_code)
#     sleep(1)

r = reqs.get(url+'IOLCP')
print(r.status_code,r.encoding)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

