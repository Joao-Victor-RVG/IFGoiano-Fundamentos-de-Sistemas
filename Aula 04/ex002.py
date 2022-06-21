from re import X
from reportlab.pdfgen import canvas


def GeneratePDF():
    try:
        nome_pdf = input('informe o nome do PDF:\n')
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        lista = {}
        while idade != 0:
            nome = lista.append(input())
            idade = lista.append(input())
            for nome, idade in lista.items():
                x -=20
                pdf.drawString(247, X, '{}:{}'.format(nome, idade))
        pdf.setTitle(nome_pdf)
        pdf.setFont("helvetica", 14)
        pdf.drawString(245, 750 , "Lista de Clientes")
        pdf.setFont("Helvetica-Bold" , 12)
        pdf.drawString (245, 724, "Cliente")
        pdf.save()
        print('{}.pdf foi criado com sucesso, Parabéns meu caro aluno'.format(nome_pdf))
    except:
        print('Infelizmente você repetira a materia fundamentos de sistemas')


GeneratePDF()

