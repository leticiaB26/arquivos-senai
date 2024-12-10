#ALUNA:LETICIA DA VEIGA

from tkinter import*
import tkinter

i = Tk()
i.title("programa financeiro")
i.geometry("800x600+250+30")
i.wm_iconbitmap('icone.ico')

lb1 = Label(i,text="label 1", bg="yellow")
lb1.place(x=230,y=200)

lb2 = Label(i,text="label 2", bg="red")
lb2.place(x=230,y=200)

lb3 = Label(i,text="label 3", bg="pink")
lb3.place(x=230,y=200)

lb4 = Label(i,text="label 4", bg="green")
lb4.place(x=230,y=200)

# com LEFT E "left", os objetos ficam somente a esquerda no centro, e o anchor ficam a esquerda  em cima da tela
# lb4.pack(side=LEFT)
# lb2.pack(side="left")
# lb3.pack(anchor="w")
# lb1.pack(side=BOTTOM,anchor= "e")

lb4.pack(side=LEFT)
lb2.pack(side="left")
lb3.pack(anchor="w")
lb1.pack(side=BOTTOM,anchor=CENTER)


i.mainloop()