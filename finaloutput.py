import TradingWithCrossRef as Tr
import pandas_datareader as dr
import pandas as pd
import utils4stocks as utils

# alist = Tr.getBuys()

alist = ['ETRN','F',"ESPR","DXC"]
for tick in alist:
    df = utils.dfmanip(tick,200)
    if df.shape[0] < 200:
        Length = str(df.shape[0]) + " day"
    else:
        Length = "200 day"
    movingaverage = df.iloc[-1]['MA']
    
    
    price = df.iloc[-1]['Close']

    utils.percent(tick,price,movingaverage,Length)
    print(df[-2:], end = "\n\n")


