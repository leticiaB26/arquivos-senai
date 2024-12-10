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

#a funçao pack posiciona o objeto, posiciona o objeto e segue a ordem delcarada 
#lb4.pack()
#lb2.pack()
#lb3.pack()
#lb1.pack()

#parametro side seguido de um posicao posiciona o objeto coforme ardem declarada no parametro
# lb4.pack(side="top")
# lb2.pack(side="left")
# lb3.pack(side="right")
# lb1.pack(side="bottom")

#"in de left e de rait" by:tite
lb4.pack(side="left")
lb2.pack(side="left")
lb3.pack()
lb1.pack()



i.mainloop()