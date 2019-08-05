from selenium import webdriver
import TradingWithCrossRef as Tr
import pandas_datareader as dr
import pandas as pd
import utils4stocks as utils

# alist = Tr.getBuys()

chrome_path = r"C:\Users\u15866\OneDrive - Kimberly-Clark\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

alist = ["ETRN", "spxu"]


def price2MA(alist):
    alist = set(alist)    
    for tick in alist:
        URL = "https://www.barchart.com/stocks/quotes/" +tick+"/technical-analysis"
        driver.get(URL)
        try:
            MA = driver.find_element_by_xpath("""//*[@id="main-content-column"]/div/div[2]/div/div[1]/div/div/ng-transclude/table/tbody/tr[5]/td[2]""")
            Length = "200 day"
            Lengthforcalc = 200
            if MA.text == "N/A":
                print("200 day not found for "+tick+ ", moving to 100 day")
                MA = driver.find_element_by_xpath("""//*[@id="main-content-column"]/div/div[2]/div/div[1]/div/div/ng-transclude/table/tbody/tr[4]/td[2]""")
                Length = "100 day" 
                Lengthforcalc = 100                
        except:
            print("continued at MA" + tick)
            continue

        try:
            price = driver.find_element_by_xpath("""//*[@id="main-content-column"]/div/div[1]/div[3]/div[3]/span[1]""")           
        except:
            try: 
                price = driver.find_element_by_xpath("""//*[@id="main-content-column"]/div/div[1]/div[3]/div[2]/span[1]""")
            except:
                print("continued at price" + tick)
                continue

        try:
            utils.percent(tick,price.text,MA,Length)
            
        except:
            print("continued at percent" + tick)
            continue
        df = utils.dfmanip(tick,Lengthforcalc)
        print(df[-5:])

    driver.close()



price2MA(alist)


