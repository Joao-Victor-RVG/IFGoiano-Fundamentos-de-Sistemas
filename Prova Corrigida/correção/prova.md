

# Questão 01
1- import psutil   
2- bateria = psutil.sensor_battery()
3- nivel = str(bateria.percent)
4- print(f'No momento você tem {nivel}$')


# Explicação:
1- Uso da biblioteca psutil atraves do import, a biblioteca é usada para a ultilização de recursos de indentificação de sensores e coleta de dados dos mesmo de um hardware de computador atráves do Python

2- Variavel ultilizada para coletar informações do sensor da bateria

3- variavel ultilizada para coletar o dado de porcentagem de bateria do device

4- Função print que irá retornar os valores coletados das duas variaveis anteriores e irá mostrar para o usuario
# Função do script:
O script da questão 1 tem a função de coletar dados de sensores presentes no hardware do seu computador e retornar valores a partir disso, o script em especifico retorna os valores de porcentagem de bateria para o usuario.

# Questão 02
1- from barcode import EAN13
2- from barcode.writer import ImageWriter

3- with open(r'C:\Users\Mather\.vscode\Codigo barra\teste4.png', 'wb') as file:
4-    EAN13('123456789111', writer=ImageWriter()).write(file)
# Explicação:
1- Barcode é uma biblioteca Python que tem como função auxiliar na criação de um codigo de barras

2- e na linha "1" e "2" podemos ver que o script solicitou funções especificas da biblioteca a partir do "import"

3 - Na linha 3 os comandos digitados irão criar um arquivo ".PNG"  no local indicado e a função "open" irá abrir esse arquivo assim que o script for executado

4- Na linha 4 o codigo presente irá colocar todos os dados que foi solicitado dentro do codigo de barras
# Função do script:
O script tem a função de gerar codigos de barra a partir de um script em python

# Questão 03 

1- from bs4 import BeautifulSoup
2- import requests


3- html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/1021/morrinhos-go').content


4- soup = BeautifulSoup(html, 'html.parser')


5- resumo = soup.find(class_='-gray -line-height-24 _center')


6- tempMin = soup.find(id = 'min-temp-1')
7- tempMAx = soup.find(id = 'max-temp-1')


8-   print(' Resumo:'+ resumo.text)
9-   print('Temp. Minima:'+ tempMin.string)
10- print('Temp. Máxima:'+tempMAx.string)

# Explicação:

1- Biblioteca "Bs4" é uma biblioteca Python de extração de dados de arquivos HTML e XML.

2- Função Import requests é uma biblioteca Python que tem a função de importar funções para o python para a realização de solicitações de x naturezas

3- Função HTML usada para colocar as informações recebidas da API em um arquivo HTML

4- Beautiful Soup é um pacote Python para analisar documentos HTML e XML.

5- Função do pacote BeautifulSoup para editar o conteudo HTML 

6- Puxar as informações de temperatura minima de uma localidade pela API

7- Puxar as informações de temperatura Maxima de uma localidade pela API

8- Função print irá mostrar para o usuario o resumo do arquivo HTML gerado

9- Irá mostrar para o usuario a temperatura Minima que a API forneceu 

10- Irá mostrar para o usuario a temperatura maxima que a API forneceu



