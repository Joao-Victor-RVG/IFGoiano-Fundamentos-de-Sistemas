
from reportlab.pdfgen import canvas  # biblioteca python usada para gerar o arquivo PDF solicitado

#criando a função "GeneratePDF"
def GeneratePDF(lista):
    try:
        nome_pdf = input('Informe o nome do PDF: ')
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for nome,idade in lista.items():
            x -= 20
            pdf.drawString(247,x, '{} : {}'.format(nome,idade))
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,750, 'Lista de Convidados')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245,724, 'Nome e idade')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))
#criando duas listas para receber os valores solicitados pelo usuario
entrada = []
lista = []
while entrada != 0: #while usado devido não saber a quantidade de repetições que o usuario deseja 
    entrada = input('Digite os itens desejador no PDF')
    lista.append(entrada)

GeneratePDF(lista)
