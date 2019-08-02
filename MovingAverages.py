from selenium import webdriver
import TradingWithCrossRef as Tr
import pandas as pd

alist = Tr.getBuys()

chrome_path = r"C:\Users\u15866\OneDrive - Kimberly-Clark\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

# alist = ["ETRN","FLLCU","FLLCU","GRA","USAK",]


def price2MA(alist):
    alist = set(alist)
    ticklist = []
    MAlist = []
    pricelist = []
    for tick in alist:
        URL = "https://www.barchart.com/stocks/quotes/" +tick+"/technical-analysis"
        driver.get(URL)

        try:
            MA = driver.find_element_by_xpath("""//*[@id="main-content-column"]/div/div[2]/div/div[1]/div/div/ng-transclude/table/tbody/tr[5]/td[2]""")
            MAlist.append(MA.text)
        except:
            continue

        try:
            price = driver.find_element_by_xpath("""//*[@id="main-content-column"]/div/div[1]/div[3]/div[2]/span[1]""")
            pricelist.append(price.text)
            ticklist.append(tick)
        except:
            continue

        try:
            percent(tick,price.text,MA.text)
        except:
            print("something went wrong, continuing")
            continue

    
def percent(Ticker, Price, MA):
    if MA == 'N/A':
        movA = float(1)
    else:
        movA = float(MA)
          
    result = (float(Price) - movA) / movA * 100
    if result > 0:
        aorb = "above"
    else:
        aorb = "below"
    print(Ticker +" is trading at " +str(round(result,2)).replace("-","")+"% " +aorb +" the 200 day moving average")


price2MA(alist)


