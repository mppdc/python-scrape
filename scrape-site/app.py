from selenium import webdriver
import os
import time

driver = webdriver.Chrome(executable_path=os.getcwd() + os.sep + 'chromedriver')
driver.get ('https://www.heise.de/download/search#?page=1&sort=DOWNLOADRANK')

time.sleep (4)
botao_acept = driver.find_element_by_xpath('//button[@class="sc-bqGHjH qNjkR"]')
botao_acept.click()
time.sleep (4)
titulos2 = driver.find_element_by_xpath('//h3[@class="gamma ng-binding"]')

for titulo in titulos2:
    print (titulo.text)