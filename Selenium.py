import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.sofascore.com/tr/football/match/fenerbahce-trabzonspor/blbsclb#id:12530873")

ennesyri_elements = driver.find_elements(By.XPATH, "//a[@class='sc-5d0212b8-0 fpvGGR']")

touch = ennesyri_elements[21]

touch.click()

time.sleep(1)
elements_column = driver.find_elements(By.XPATH, "//div[@class='Box Flex dlyXLO bnpRyo']//div[@class='Text dgWCMi']")
elements_index = driver.find_elements(By.XPATH, "//div[@class='Box Flex dlyXLO bnpRyo']//span[@class='Text iescdy']")
time.sleep(1)
driver.execute_script("arguments[0].scrollIntoView();", elements_column[1]) #sayfayı aşağı kaydırmaya yarıyor
time.sleep(1)
data_column = []
data_index = []
count = 1
for i in range(1, 25):
    if i % 10 == 0:
        driver.execute_script("arguments[0].scrollIntoView();", elements_column[i * count])
        # sayfayı aşağı kaydırmaya yarıyor
        driver.execute_script("arguments[0].scrollIntoView();", elements_index[i * count])
    data_column.append(elements_column[i].text)
    data_index.append(elements_index[i].text)

df = pd.DataFrame([data_index], columns=data_column)
df.to_csv('ennesyri_selenium.csv', index=False)