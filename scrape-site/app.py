from selenium import webdriver
import os

driver = webdriver.Chrome(executable_path=os.getcwd() + os.sep + 'chromedriver')
driver.get ('https://www.heise.de/download/search#?page=1&sort=DOWNLOADRANK')


titulos = driver.find_element_by_xpath('//h3[@class="gamma ng-binding"]')

for titulo in titulos
    print (titulo.text)