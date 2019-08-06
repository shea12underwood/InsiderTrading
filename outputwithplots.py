# import TradingWithCrossRef as Tr
import pandas_datareader as dr
import pandas as pd
import utils4stocks as utils
import matplotlib.pyplot as plt 
from matplotlib import style
from datetime import date, timedelta
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
style.use('ggplot')
# alist = Tr.getBuys()

alist = ['BBBY']
for tick in alist:
    df = dr.data.get_data_yahoo(tick,start = date.today() - timedelta(300) , end = date.today())
    df = utils.exponential_moving_average(df,180)
    df = utils.moving_average(df,200)
    df = utils.macd(df,12,26)
    print(df)
    
    ax1 = plt.subplot2grid((20,1) , (0,0) , rowspan = 15, colspan =1)
    ax2 = plt.subplot2grid((20,1) , (15,0) , rowspan = 5, colspan =1, sharex=ax1)
   
    
    ax1.plot(df.index, df['Close'])
    ax1.plot(df.index, df['MA'])
    ax2.plot(df.index, df['MACD_12_26'])
    ax2.plot(df.index, df['MACDsign_12_26'])
    
    

    plt.show()
    



