from barcode import EAN13
from barcode.writer import ImageWriter

#Gerar o codigo de barras e salvar em um caminho desejado
with open(r'C:\Users\Mather\.vscode\Codigo barra\teste4.png', 'wb') as file:
    EAN13('123456789111', writer=ImageWriter()).write(file)
