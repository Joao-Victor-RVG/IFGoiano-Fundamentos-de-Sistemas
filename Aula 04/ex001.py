
import requests 
#
url = 'https://economia.awesomeapi.com.br/all/USD-BRL'
#
resposta = requests.get(url)
#
valor_em_reais = float(input())
#
if resposta.status_code == 200:
    dolar_value=float(resposta.json()['USD']['ask'])     # importa dados do json 
    print(f'o valor do dollar em R${dolar_value}')       # escreve o valor do dollar em reais
# resultado do valor em reais vezes o valor do dollar atualizado  
valor_convertido=valor_em_reais *dolar_value
print("{:.2f}".format(valor_convertido))






