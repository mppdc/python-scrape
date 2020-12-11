from selenium import webdriver
import os
import time

driver = webdriver.Chrome(executable_path=os.getcwd() + os.sep + 'chromedriver')
driver.get ('https://www.heise.de/download/search#?page=1&sort=DOWNLOADRANK')
#driver.get ('https://www.globo.com/')

time.sleep (4)
botao_acept = driver.find_elements_by_xpath('//button[@data-testid="uc-accept-all-button"]')
#botao_acept = driver.find_element_by_xpath('//a[@class="hui-premium__link"]')
for bot in botao_acept:
    bot.click()
time.sleep (4)
titulos = driver.find_elements_by_xpath('//h3[@class="gamma ng-binding"]')

for titulo in titulos:
    print (titulo.text)