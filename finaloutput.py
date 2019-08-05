import TradingWithCrossRef as Tr
import pandas_datareader as dr
import pandas as pd
import utils4stocks as utils

# alist = Tr.getBuys()

alist = ['ETRN','F',"ESPR","DXC"]
for tick in alist:
    df = utils.dfmanip(tick,200)
    movingaverage = df.iloc[-1]['MA']
    Length = "200 day"
    if str(movingaverage) == "nan":
        df = utils.dfmanip(tick,100)
        movingaverage = df.iloc[-1]['MA']
        Length = "100 day"
    
    price = df.iloc[-1]['Close']

    utils.percent(tick,price,movingaverage,Length)
    print(df[-2:], end = "\n\n")
