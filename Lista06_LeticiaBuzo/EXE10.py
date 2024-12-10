#ALUNA:LETICIA DA VEIGA

from tkinter import *

i = Tk()

i.title("Programa Financeiro")
i.geometry("800x600+250+40")
i.wm_iconbitmap('icone.ico')

# A VARIAVEL lb É REFERENTE A LABELS
lb1 = Label(i, text="LOGIN", bg="yellow")
# O COMPONENTE .grid SERVE TAMBEM PARA POSICIONAR UTILIZANDO INDICATIVO DE linha (row) E COLUNA (column).
lb1.grid(row=1,column=1)


lb2 = Label(i, text="SENHA", bg="red")
lb2.grid(row=2,column=1)

ed1 = Entry(i)
ed1.grid(row=1,column=2)


ed2 = Entry(i)
ed2.grid(row=2,column=2)


bt1 = Button(i, text="Login")
bt1.grid(row = 4, column=2)




i.mainloop()