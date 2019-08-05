from selenium import webdriver
import TradingWithCrossRef as Tr
import pandas as pd

alist = Tr.getBuys()

chrome_path = r"C:\Users\u15866\OneDrive - Kimberly-Clark\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

# alist = ["ETRN","FLLCU","FLLCU","GRA","USAK",]


def price2MA(alist):
    alist = set(alist)    
    for tick in alist:
        URL = "https://www.barchart.com/stocks/quotes/" +tick+"/technical-analysis"
        driver.get(URL)
        try:
            MA = driver.find_element_by_xpath("""//*[@id="main-content-column"]/div/div[2]/div/div[1]/div/div/ng-transclude/table/tbody/tr[5]/td[2]""")
            Length = "200 day"
            if MA.text == "N/A":
                print("200 day not found for "+tick+ ", moving to 100 day")
                MA = driver.find_element_by_xpath("""//*[@id="main-content-column"]/div/div[2]/div/div[1]/div/div/ng-transclude/table/tbody/tr[4]/td[2]""")
                Length = "100 day"                 
        except:
            print("continued at MA" + tick)
            continue

        try:
            price = driver.find_element_by_xpath("""//*[@id="main-content-column"]/div/div[1]/div[3]/div[3]/span[1]""")
            
        except:
            print("continued at price" + tick)
            continue

        try:
            percent(tick,price.text,MA.text,Length)
            
        except:
            print("continued at percent" + tick)
            continue
    driver.close()
def percent(Ticker, Price, MA, Length):
    if MA == 'N/A':
        movA = float(1)
    else:
        movA = float(MA)
          
    result = (float(Price) - movA) / movA * 100
    if result > 0:
        aorb = "above"
    else:
        aorb = "below"
    print(Ticker +" is trading at " +str(round(result,2)).replace("-","")+"% " +aorb +" the "+ Length+" moving average")


price2MA(alist)


