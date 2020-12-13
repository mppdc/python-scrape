from selenium import webdriver
from PIL import Image
import requests
import re
import os
import time
import urllib
import json
from pathlib import Path

driver = webdriver.Chrome(executable_path=os.getcwd() + os.sep + 'chromedriver')
driver.get ('https://www.heise.de/download/search#?page=1&sort=DOWNLOADRANK')
#driver.get ('https://www.globo.com/')

time.sleep (8)
#botao_acept = driver.find_elements_by_xpath('//button')
#botao_acept = driver.find_element_by_xpath('//a[@class="hui-premium__link"]')
#for bot in botao_acept:
#    bot.click()
#time.sleep (4)

arquivo_lista = []
contador = 0


def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result


def resize_canvas(old_image_path, new_image_path, canvas_width, canvas_height):
    import math
    """
    Resize the canvas of old_image_path.

    Store the new image in new_image_path. Center the image on the new canvas.

    Parameters
    ----------
    old_image_path : str
    new_image_path : str
    canvas_width : int
    canvas_height : int
    """
    im = Image.open(old_image_path)
    old_width, old_height = im.size

    # Center the image
    x1 = int(math.floor((canvas_width - old_width) / 2))
    y1 = int(math.floor((canvas_height - old_height) / 2))

    mode = im.mode
    if len(mode) == 1:  # L, 1
        new_background = (255)
    if len(mode) == 3:  # RGB
        new_background = (255, 255, 255)
    if len(mode) == 4:  # RGBA, CMYK
        new_background = (255, 255, 255, 255)

    newImage = Image.new(mode, (canvas_width, canvas_height), new_background)
    newImage.paste(im, (x1, y1, x1 + old_width, y1 + old_height))
    newImage.save(new_image_path)


def mostra_resultado(contador):
    titulos = driver.find_elements_by_xpath('//h3[@class="gamma ng-binding"]')
    imagens = driver.find_elements_by_xpath('//img[@class="recommend-apps__slider-image"]')
    for titulo in titulos:
        arquivo_lista.append({'titulo':titulo.text, 'imagem':''})
        print (titulo.text)
    for imagem in imagens:
        src = imagem.get_attribute('src')
        pos = src.rfind("/") 
        nome = src[pos+1:len(src)]
        for indice, item in enumerate(arquivo_lista):
            a = arquivo_lista[indice]
            if a['imagem'] == '':
                imagem_lista = arquivo_lista[indice]
                imagem_lista['imagem']= nome
                break
        r = requests.get(src, allow_redirects=True)
        nome = 'imagens/'+nome
        print (nome)
        open(nome, 'wb').write(r.content)
        contador += 1

        # Conversão

        img_convert = Image.open (nome)
        img_nova = expand2square(img_convert, (255,255,255)).resize((200,200))
        img_nova.save(nome)

def grava_arquivo():
    arquivos_json = json.dumps(arquivo_lista)
    Path('heise.de-downloads.json').write_text(arquivos_json)
    #print (arquivo_lista)

mostra_resultado(0)
time.sleep (5)

while True:
    try:
        prox_pag = driver.find_element_by_xpath('//i[@class="icon-angle-right"]')
        prox_pag.click()
        time.sleep (15)
        mostra_resultado(contador)
        grava_arquivo()
    except:
        break



grava_arquivo()


