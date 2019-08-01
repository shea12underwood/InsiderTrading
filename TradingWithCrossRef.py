from selenium import webdriver
import pandas as pd


def getBuys(numpages=1):
    stocklist = []
    positionlist = []
    filingtime = []
    pricelist = []
    sharepricelist = []
    datelist = []
    chrome_path = r"C:\Users\u15866\OneDrive - Kimberly-Clark\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    URL = "https://www.insidearbitrage.com/insider-buying/"
    driver.get(URL)
    


    for i in range(2,102):
        ticker = driver.find_element_by_xpath("""//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[""" + str(i) + """]/td[2]/a""")
        stocklist.append(ticker.text)
    
    for i in range(2,102):
        position = driver.find_element_by_xpath("""//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[""" + str(i) + """]/td[4]""")
        positionlist.append(position.text)
        
    for i in range(2,102):
        time = driver.find_element_by_xpath("""//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[""" + str(i) + """]/td[10]/span/a""")
        filingtime.append(time.text)
        
    finallist = list(zip(stocklist,positionlist,filingtime))

    print(finallist)
    
getBuys()


