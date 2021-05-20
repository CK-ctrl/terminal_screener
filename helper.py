from nsetools import Nse
from pprint import pprint

nse = Nse()
Stocks = nse.get_stock_codes()

n = len(Stocks)
print("Number of stocks: ",n)