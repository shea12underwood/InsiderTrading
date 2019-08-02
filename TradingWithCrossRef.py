from selenium import webdriver
import pandas as pd


def getBuys(numpages=1):
    stocklist = []
    positionlist = []
    valuelist = []
    costlist = []
    datelist= []
    chrome_path = r"C:\Users\u15866\OneDrive - Kimberly-Clark\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    URL = "https://www.insidearbitrage.com/insider-buying/"
    driver.get(URL)
    

    counter = 0
    while counter < numpages:

        if counter != 0:
            nextbutton = driver.find_element_by_xpath("""//*[@id="sortTableM"]/div[2]/table[3]/tbody/tr/td/a[1]""")
            nextbutton.click()

        for i in range(2,102):
            position = driver.find_element_by_xpath("""//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[""" + str(i) + """]/td[4]""")
            if "C" in position.text:
                pass
            else:
                continue
            positionlist.append(position.text)

            ticker = driver.find_element_by_xpath("""//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[""" + str(i) + """]/td[2]/a""")
            stocklist.append(ticker.text)

            value = driver.find_element_by_xpath("""//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[""" + str(i) + """]/td[8]""")
            valuelist.append(value.text)

            cost = driver.find_element_by_xpath("""//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[""" + str(i) + """]/td[6]""")
            costlist.append(cost.text)

            date = driver.find_element_by_xpath("""//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[""" + str(i) + """]/td[5]/span""")
            datelist.append(date.text)
        
        counter +=1
        print(positionlist)

    driver.close()

    finallist = list(zip(stocklist,positionlist,valuelist,costlist,datelist))

    df = pd.DataFrame(finallist, columns=["ticker", "position", "totalcost", "shareprice","date"])

    returnlist=[]
    for index, row in df.iterrows():
        if "C" in row["position"]:
            psize = row["totalcost"]
            psize = psize.replace(",", "")
            if float(psize) > 100_000:
                print(row['ticker'] +": On " + row['date'] + ", The " + row['position'] +" bought " + row['totalcost'] + " worth of shares at a price of " +row['shareprice'] + " per share.")
                returnlist.append(row['ticker'])
    return returnlist
    

if __name__ == "__main__":
    getBuys()

