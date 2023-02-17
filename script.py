import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import os
import subprocess

#/dashboard?id=test1
#//*[@id="tabpanel-overall"]/div[4]/div[2]/a
userName="admin"
password="123ASqwezxc"
driver = webdriver.Chrome()
url = "http://localhost:9000/projects?sort=-name"
driver.get(url)
dir_path = r'C:\Users\zkus\Downloads\Windows-universal-samples-main\Samples'

time.sleep(10)

oturumac = driver.find_element(By.XPATH, '//*[@id="login"]')
oturumac.click()
oturumac.send_keys(userName)

sifregir = driver.find_element(By.XPATH, '//*[@id="password"]')
sifregir.click()
sifregir.send_keys(password)

girisyapbuton = driver.find_element(By.XPATH, '//*[@id="login_form"]/form/div[3]/div/button')
girisyapbuton.click()
i=0
time.sleep(10)





for foldername in os.listdir(dir_path):
    if os.path.isdir(os.path.join(dir_path, foldername)):
        CreateProject = driver.find_element(By.XPATH,
                                            '//*[@id="projects-page"]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/button')
        CreateProject.click()
        time.sleep(10)
        ProjectName = driver.find_element(By.XPATH, '//*[@id="project-name"]')
        ProjectNameButton = driver.find_element(By.XPATH, '//*[@id="create-project"]/div/div/form/button')
        ProjectName.click()
        ProjectName.send_keys(foldername)
        ProjectNameButton.click()
        time.sleep(10)
        RepoAnalysis = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div/div/div[2]/button')
        RepoAnalysis.click()
        time.sleep(10)
        TokenCreatorButton = driver.find_element(By.XPATH,
                                                 '//*[@id="container"]/div/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div/form/div[2]/div/button')
        TokenCreatorButton.click()
        time.sleep(10)
        TokenProvider = driver.find_element(By.XPATH,
                                            '//*[@id="container"]/div/div[2]/div/div[2]/div[3]/div/div[2]/button')
        TokenProvider.click()
        DotNetSelector = driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[2]/div/div[3]/div[3]/div/div/div/ul/li[3]/button')
        DotNetSelector.click()
        firstCommand = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div/div[3]/div[3]/div/div/div[2]/div[2]/div[3]/pre/text()').text
        secondCommand = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div/div[3]/div[3]/div/div/div[2]/div[2]/div[4]/pre').text
        thirdCommand = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div/div[3]/div[3]/div/div/div[2]/div[2]/div[5]/pre/text()').text
        subprocess.run(firstCommand, shell=True)
        subprocess.run(secondCommand, shell=True)
        subprocess.run(thirdCommand, shell=True)
        returnProject = driver.find_element(By.XPATH, '//*[@id="global-navigation"]/div/div/ul/li[1]/a')
        returnProject.click()


time.sleep(10)
