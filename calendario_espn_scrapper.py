from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep
import csv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
import re

#Script para criar um dicionário com o nome do time e o link para seu calendário de jogos

driver = webdriver.Edge()
# Abre a página principal
driver.get("https://www.espn.com.br/futebol/equipos/_/liga/uefa.europa.conf")
sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')

# Encontrar os links <a> com a classe "AnchorLink"
links = soup.find_all('a', class_='AnchorLink', string='Calendário')

calendarios = {}

for link in links:
    url = link.get('href')
    nome_time = url.split('/')[-1]  # Pega a última parte do link (nome do time)
    calendarios[nome_time] = url

# Exibir o dicionário
print(calendarios)
# Fechar o driver
driver.quit()
