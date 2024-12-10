#------priemeira tela widget-----------#
#------aluna leticia buzo--------------#

#o comando abaixo importa tudo da biblioteca que é necessário para a ciração de telas

from cgitb import text
from tkinter import *

# i (instanciar) recebe o objeto tk
i = Tk()

#o código gera o titulo da janela
i.title('programa financeiro')

#propriedade que altera o tamanho da janela (980x720) e a distancia da direita e topo da tela (250x30)
i.geometry('1080x960+290+60')

#proproedades graficas, cor de fundo da tela (bg) ou (background) não pode passar o i com ponto (i.)

i["bg"] = "pink"

#crai o icone na janela, voce deve ter a imagem no mesmo local do codigo
i.wm_iconbitmap('icone.ico')
lb = Label(i,text='nome do usuario')
lb.place(x=100, y=100)

lb = Label(i,text='Leticia Buzo')
lb.place(x=110, y=150)

#cria um botao e posiicona (place) ele em relaçaõ a label
bt = Button(i,width='20', text='ok')
bt.place(x=230, y=100)

#gera a janela grafica
i.mainloop()