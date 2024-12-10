# ----------botão com função---------#
# aluna leticia buzo

from tkinter import *

# CRIANDO UMA FUNCAO PARA CLIQUE NO BOTAO

def bt_click():
    # O label QUE USA PROPRIEDADE text RECEBERÁ A MENSAGEM "trocou o texto" 
    lb["text"]="Trocou o texto"
    # ESSE print EXIBE O TEXTO NA TELA DO CONSOLE
    print("O botão foi clicado")

def bt_clickar():
    # ESSE PRINT EXIBE O TEXTO DIGITADO NA CAIXA DE TEXTO
    # EXIBE NA LABEL DA TELA
    print(ed.get())
    lb["text"] = ed.get 

i=Tk()

i.title('Programa Financeiro')

i.geometry('980x720+250+30')

i["bg"]="pink"

i.wm_iconbitmap('icone.ico')

lb = Label(i, text='Nome do Usuario')
lb.place(x=100,y=100)

bt = Button(i, width="20", text='OK', command=bt_click)
bt.place(x=230,y=100)

# CRIA UM botao E POSICIONA ABAIXO DO BOTAO ok
bt = Button(i, width="20", text='OK', command=bt_click)
bt.place(x=230,y=100)

ed = Entry(i)
ed.place(x=230,y=150)

# GERA A JANELA GRAFICA
i.mainloop()