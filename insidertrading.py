# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 09:06:46 2019

@author: u15866
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

def getinsiders(numpages):
    stocklist = []
    insiderlist=[]
    costlist=[]
    pricelist=[]
    sharepricelist=[]
    datelist=[]
    chrome_path = r"C:\Users\u15866\OneDrive - Kimberly-Clark\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    URL = "https://www.gurufocus.com/insider/summary"
    
    driver.get(URL)
    
    counter = 0
    while counter < numpages:


        tickernames = driver.find_elements_by_class_name("table-stock-info")
        for ticker in tickernames:
            stocklist.append(ticker.text)
            
        insiderpositions = driver.find_elements_by_class_name("table-position-info")
        for insider in insiderpositions:
            insiderlist.append(insider.text)
        
        for i in range(1,41):
            cost = driver.find_element_by_xpath("""//*[@id="wrapper"]/div/table/tbody/tr["""+str(i)+"""]/td[12]""")
            costlist.append(cost.text)
        
        for i in range(1,41):
            price = driver.find_element_by_xpath("""//*[@id="wrapper"]/div/table/tbody/tr["""+str(i)+"""]/td[4]/span""")
            pricelist.append(price.text)

        for i in range (1,41):
            shareprice = driver.find_element_by_xpath("""//*[@id="wrapper"]/div/table/tbody/tr["""+str(i)+"""]/td[11]""")
            sharepricelist.append(shareprice.text)

        purchasedates = driver.find_elements_by_class_name("table-date-info")
        for date in purchasedates:
            datelist.append(date.text)

        counter+=1
        nextbutton = driver.find_element_by_xpath("""//*[@id="components-root"]/div/section/main/div[7]/div/button[2]/i""")
        nextbutton.click()

    driver.close()
    intrades = list(zip(stocklist,insiderlist,costlist,pricelist,sharepricelist,datelist))
#    print(intrades)
    
    df = pd.DataFrame(intrades, columns = ['ticker', 'position', 'position size','price','shareprice','date'])
    
    for index, row in df.iterrows():
        if "C" in row['position']:
            psize = row['position size']
            psize = psize.replace(",","")
            if float(psize) > 100_000:
                print(row['ticker'], end=": ")
                print("On "+row['date'] + ", The "+row['position']+" spent "+psize + " at a price of "+row['shareprice']+ " per share. " + row['ticker']+ " is now trading at " + row['price'] + " per share.")
                print("\n")
                
               


getinsiders(2)  