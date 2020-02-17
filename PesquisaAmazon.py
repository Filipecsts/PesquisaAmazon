#@Autor: Filipe Conceição dos Santos
#Data: 06/02/2020

import time
import csv
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as presente
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='ChromeDriver\chromedriver.exe')

aguardar = WebDriverWait(driver, 15)

driver.get('http://amazon.com')
campoTexto = aguardar.until(presente.presence_of_element_located((By.NAME, 'field-keywords')))
campoTexto.send_keys('iphone')
btnPesquisar = aguardar.until(presente.presence_of_element_located((By.CLASS_NAME, 'nav-input')))
btnPesquisar.click()

def LocalizarDado(xpath):
    info=driver.find_element_by_xpath(xpath).get_attribute('innerHTML')
    return info

def SalvarEmCSV(dados):
    escrever.writerows([dados])

with open('pesquisa.csv', 'w', newline='', encoding='utf-8') as saida:
    escrever = csv.writer(saida, delimiter=';')

    numBusca = 1
    numProds = int(LocalizarDado("//div[@class='a-section a-spacing-small a-spacing-top-small']/span")[2:4])

    while numBusca <= numProds:
        try:
            nProd = LocalizarDado(f'//div[@class="s-result-list s-search-results sg-row"]/div[{numBusca}]//span[@class="a-size-medium a-color-base a-text-normal"]')
        except:
            nProd = LocalizarDado(f'//div[@class="s-result-list s-search-results sg-row"]/div[{numBusca}]//span[@class="a-size-base-plus a-color-base a-text-normal"]')
        try:
            vProd = LocalizarDado(f"//div[@class='s-result-list s-search-results sg-row']/div[{numBusca}]//span[@class='a-price']/span")
        except:
            vProd = LocalizarDado(f"//div[@class='s-result-list s-search-results sg-row']/div[{numBusca}]//span[@class='a-color-base']")

        numBusca+=1
        print(f'{nProd} = {vProd}')

        titulos = ['Produto', 'Preço']
        SalvarEmCSV(titulos)
        dados = [(nProd),(vProd)]
        SalvarEmCSV(dados)

driver.close()