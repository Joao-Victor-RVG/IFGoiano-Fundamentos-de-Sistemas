from re import A
from sqlite3 import Time
from time import time
from bs4 import BeautifulSoup
import requests

Time = requests.get('https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/').content
pontos = requests.get('https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/').content

soup_time = BeautifulSoup(Time, 'html.parser')
soup_pontos = BeautifulSoup(pontos, 'html.parser')

lider = soup_time.find(class_='main team-name')
pontos = soup_pontos.find('table', attrs={'class':'lineItemsTable'})


print('Time na liderança :'+ lider.text, end = '')
print('Pontos do lider:'+ pontos.text)

