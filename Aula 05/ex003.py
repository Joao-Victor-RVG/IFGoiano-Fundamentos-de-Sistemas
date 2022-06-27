#importando bibliotecas
from bs4 import BeautifulSoup
import requests

#resgate do link do site
html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/1021/morrinhos-go').content

#aplicando biblioteca importada
soup = BeautifulSoup(html, 'html.parser')

#Resgatando a classe do texto atraves do 'find'
resumo = soup.find(class_='-gray -line-height-24 _center')

#Resgatando o 'id' da temperatura
tempMin = soup.find(id = 'min-temp-1')
tempMAx = soup.find(id = 'max-temp-1')

#Mostrando o resultado na tela
print(' Resumo:'+ resumo.text)
print('Temp. Minima:'+ tempMin.string)
print('Temp. Máxima:'+tempMAx.string)
