#ALUNA:LETICIA DA VEIGA

from tkinter import *
i = Tk()

i.title("Programa Financeiro")
i.geometry("800x600+250+30")
i.wm_iconbitmap('icone.ico')

# A VARIAVEL lb É REFERENTE A LABELS
lb1 = Label(i, text="leticia", bg="pink")
# O COMPONENTE .grid SERVE TAMBEM PARA POSICIONAR UTILIZANDO INDICATIVO DE linha (row) E COLUNA (column).
lb1.grid(row=5,column=5)


lb2 = Label(i, text="buzo", bg="grey")
lb2.grid(row=6,column=5)

ed1 = Entry(i)
ed1.grid(row=5,column=6)


ed2 = Entry(i)
ed2.grid(row=6,column=6)

lb2 = Label(i, text="")
lb2.grid(row=7,column=1)


bt1 = Button(i, text="Login")
bt1.grid(row = 7, column=6)


i.mainloop()
