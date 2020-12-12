from selenium import webdriver
from PIL import Image
import requests
import re
import os
import time
import urllib

driver = webdriver.Chrome(executable_path=os.getcwd() + os.sep + 'chromedriver 2')
driver.get ('https://www.heise.de/download/search#?page=1&sort=DOWNLOADRANK')
#driver.get ('https://www.globo.com/')

time.sleep (8)
#botao_acept = driver.find_elements_by_xpath('//button')
#botao_acept = driver.find_element_by_xpath('//a[@class="hui-premium__link"]')
#for bot in botao_acept:
#    bot.click()
#time.sleep (4)

def mostra_resultado():
    titulos = driver.find_elements_by_xpath('//h3[@class="gamma ng-binding"]')
    imagens = driver.find_elements_by_xpath('//img[@class="recommend-apps__slider-image"]')
    for titulo in titulos:
        print (titulo.text)
    for imagem in imagens:
        src = imagem.get_attribute('src')
#        print (src)
        pos = src.rfind("/") 
        nome = src[pos:len(src)]
        print (nome)
        r = requests.get(src, allow_redirects=True)
        nome = 'imagens'+nome
        open(nome, 'wb').write(r.content)
#        img = Image.open (src)

#        urllib.urlretrieve(src, 'imagens/' + str(i))
#        print (img.type)
#        print (img.size)


mostra_resultado()
time.sleep (5)

while True:
    try:
        prox_pag = driver.find_element_by_xpath('//i[@class="icon-angle-right11"]')
        prox_pag.click()
        time.sleep (5)
        mostra_resultado()
    except:
        break




