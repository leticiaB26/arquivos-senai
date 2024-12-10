#ALUNA:LETICIA DA VEIGA


from tkinter import*


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

#o codigo abaixo posiciona cada label em lugares diferentes

# lb1.pack(side=TOP,fill=X)#o comando fill é responsavel do preenchimento 100%, deve usar X para horizontal 
# lb2.pack(side=RIGHT,fill=Y)#o comando fill é responsavel do preenchimento 100%, deve usar Y para vertical
# lb3.pack(side=LEFT,fill=Y)
# lb4.pack(side=BOTTOM,fill=X)

# lb2.pack(side=RIGHT,fill=Y)
# lb3.pack(side=LEFT,fill=Y)#o both faz a sobreposicao na outra label
# lb1.pack(side=TOP,fill=BOTH)
# lb4.pack(side=BOTTOM,fill=BOTH)

lb1.pack(side=TOP, fill=BOTH, expand=1)
lb4.pack(side=TOP, fill=BOTH, expand=1)
lb2.pack(side=TOP, fill=BOTH, expand=1)
lb3.pack(side=TOP, fill=BOTH, expand=1)




i.mainloop()