import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

#/dashboard?id=test1
#//*[@id="tabpanel-overall"]/div[4]/div[2]/a
userName="admin"
password="123ASqwezxc"
driver = webdriver.Chrome()
url = "http://localhost:9000/dashboard?id=test1"
driver.get(url)

time.sleep(10)

oturumac = driver.find_element(By.XPATH, '//*[@id="login"]')
oturumac.click()
oturumac.send_keys(userName)

sifregir = driver.find_element(By.XPATH, '//*[@id="password"]')
sifregir.click()
sifregir.send_keys(password)

girisyapbuton = driver.find_element(By.XPATH, '//*[@id="login_form"]/form/div[3]/div/button')
girisyapbuton.click()

time.sleep(10)

CodeSmell = driver.find_element(By.XPATH, '//*[@id="tabpanel-overall"]/div[4]/div[2]/a')
CodeSmell.click()

time.sleep(10)
