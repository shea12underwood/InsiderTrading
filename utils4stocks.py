import pandas as pd 
import pandas_datareader as dr
from datetime import date, timedelta

def moving_average(df, n):
    """Calculate the moving average for the given data.
    
    :param df: pandas.DataFrame
    :param n: 
    :return: pandas.DataFrame
    """
    MA = pd.Series(df['Close'].rolling(n, min_periods=0).mean(), name='MA')
    df = df.join(MA)
    return df

def exponential_moving_average(df, n):
    """
    
    :param df: pandas.DataFrame
    :param n: 
    :return: pandas.DataFrame
    """
    EMA = pd.Series(df['Close'].ewm(span=n, min_periods=n).mean(), name='EMA_' + str(n))
    df = df.join(EMA)
    return df

def macd(df, n_fast, n_slow):
    """Calculate MACD, MACD Signal and MACD difference
    
    :param df: pandas.DataFrame
    :param n_fast: 
    :param n_slow: 
    :return: pandas.DataFrame
    """
    EMAfast = pd.Series(df['Close'].ewm(span=n_fast, min_periods=0).mean())
    EMAslow = pd.Series(df['Close'].ewm(span=n_slow, min_periods=0).mean())
    MACD = pd.Series(EMAfast - EMAslow, name='MACD_' + str(n_fast) + '_' + str(n_slow))
    MACDsign = pd.Series(MACD.ewm(span=9, min_periods=9).mean(), name='MACDsign_' + str(n_fast) + '_' + str(n_slow))
    MACDdiff = pd.Series(MACD - MACDsign, name='MACDdiff_' + str(n_fast) + '_' + str(n_slow))
    df = df.join(MACD)
    df = df.join(MACDsign)
    df = df.join(MACDdiff)
    return df

def relative_strength_index(df, n):
    """Calculate Relative Strength Index(RSI) for given data.
    
    :param df: pandas.DataFrame
    :param n: 
    :return: pandas.DataFrame
    """
    i = 0
    UpI = [0]
    DoI = [0]
    while i + 1 <= df.index[-1]:
        UpMove = df.loc[i + 1, 'High'] - df.loc[i, 'High']
        DoMove = df.loc[i, 'Low'] - df.loc[i + 1, 'Low']
        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else:
            UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0:
            DoD = DoMove
        else:
            DoD = 0
        DoI.append(DoD)
        i = i + 1
    UpI = pd.Series(UpI)
    DoI = pd.Series(DoI)
    PosDI = pd.Series(UpI.ewm(span=n, min_periods=n).mean())
    NegDI = pd.Series(DoI.ewm(span=n, min_periods=n).mean())
    RSI = pd.Series(PosDI / (PosDI + NegDI), name='RSI_' + str(n))
    df = df.join(RSI)
    return df

def percent(Ticker, Price, MA, Length):
    # if MA.text == 'N/A':
    #     movA = float(1)
    # else:
    #     movA = float(MA.text)
          
    result = (Price - MA) / MA * 100
    if result > 0:
        aorb = "above"
    else:
        aorb = "below"
    print(Ticker +" is trading at " +str(round(result,2)).replace("-","")+"% " +aorb +" the "+ Length+" moving average")

def dfmanip(tick,Lengthforcalc):   
    df = dr.data.get_data_yahoo(tick,start = date.today() - timedelta(300) , end = date.today())
    df = df.reset_index()
    df = relative_strength_index(df,14)
    df = exponential_moving_average(df,180)
    df = moving_average(df,Lengthforcalc)
    df = macd(df,12,26)
    return df

if __name__ == "__main__":
    moving_average()
    exponential_moving_average()
    macd()
    relative_strength_index()
    percent()
    dfmanip()