
# coding: utf-8

# In[1]:


from selenium import webdriver
from bs4 import BeautifulSoup
import pymysql
import numpy
import pandas as pd
import datetime
import re
import time


# In[2]:


now = datetime.datetime.now()
conn = pymysql.connect(host = '140.136.136.21', user = 'seler1', passwd = 'a123', db = 'sq_data')
cur = conn.cursor()
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://www.cnyes.com/twstock/index2real.aspx?PageIndex=1&itype=TW50&stitle=%u81fa%u7063%u4e94%u5341%u6307%u6578%u6210%u4efd%u80a1') 

# In[3]:


FullTable = pd.DataFrame(index = range(0, 0), columns = range(0, 15))
for i in range(1,4):
    BOT1 = driver.find_element_by_xpath('//*[@id="DropDownList1"]')
    BOT1.send_keys(str(i))
    soup = BeautifulSoup(driver.page_source, "html.parser")
    tbhtml = soup.findAll('table')[0]
    datatmp = []
    for TBData in tbhtml.findAll('td'):
        TarText = re.sub(',', '', TBData.text)
        TarText = re.sub('--', '0', TarText)
        datatmp.append(TarText)
    df = pd.DataFrame(index = range(0, int(len(datatmp)/14)), columns = range(0, 15))
    for j in range(0, int(len(datatmp)/14)):
        df.iloc[j, range(0, 13)] = datatmp[int(14*j+1):int(14*j+14)]
    df.iloc[0:df.shape[0],len(df.columns)-2] = now.strftime('%Y-%m-%d')
    df.iloc[0:df.shape[0],len(df.columns)-1] = now.strftime('%H:%M:%S')
    if i == 1:
        for l in range(0, df.shape[0]):
            cur.execute("INSERT INTO twinfor "+"VALUES("+
                        "'"+df.iloc[l,1]+"',"+
                        "'"+df.iloc[l,0]+"',"+
                        df.iloc[l,2]+","+
                        df.iloc[l,3]+","+
                        df.iloc[l,4]+","+
                        df.iloc[l,5]+","+
                        df.iloc[l,6]+","+
                        df.iloc[l,7]+","+
                        df.iloc[l,8]+","+
                        df.iloc[l,9]+","+
                        df.iloc[l,10]+","+
                        df.iloc[l,11]+","+
                        df.iloc[l,12]+","+
                        "'"+df.iloc[l,13]+"',"+
                        "'"+df.iloc[l,14]+"')")
        FullTable = FullTable.append(df.iloc[0:,:], ignore_index=True)
    else:
        for l in range(1, df.shape[0]):
            cur.execute("INSERT INTO twinfor "+"VALUES("+
                        "'"+df.iloc[l,1]+"',"+
                        "'"+df.iloc[l,0]+"',"+
                        df.iloc[l,2]+","+
                        df.iloc[l,3]+","+
                        df.iloc[l,4]+","+
                        df.iloc[l,5]+","+
                        df.iloc[l,6]+","+
                        df.iloc[l,7]+","+
                        df.iloc[l,8]+","+
                        df.iloc[l,9]+","+
                        df.iloc[l,10]+","+
                        df.iloc[l,11]+","+
                        df.iloc[l,12]+","+
                        "'"+df.iloc[l,13]+"',"+
                        "'"+df.iloc[l,14]+"')")
        FullTable = FullTable.append(df.iloc[1:,:], ignore_index=True)
    time.sleep(5)
conn.commit()
cur.close()
conn.close()

colN = list()
for i in tbhtml.findAll('th'):
    colN.append(i.text)
colN.append('Date')
colN.append('Time')
FullTable.columns = colN[1:]
FullTable.to_csv('/home/huang/桌面/sq/TW50/TW50.csv', index=False, header=True)

driver.quit()

