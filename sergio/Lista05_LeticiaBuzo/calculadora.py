
from tkinter import *
from turtle import width


def bt_click1():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 + num2

def bt_click():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 - num2

def bt_click2():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 * num2

def bt_click3():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 / num2   


i = Tk()
i.title("programa financeiro")
i.geometry("800x600+250+30")
i.wm_iconbitmap('icone.ico')

lb = Label(i, text='0')
lb.place(x=230, y=200)

bt = Button(i, width="20", text='subtrair', command=bt_click)
bt.place(x=230, y=230)

bt = Button(i, width="20", text='somar', command=bt_click1)
bt.place(x=230, y=300)

bt = Button(i, width="20", text='multiplicar', command=bt_click2)
bt.place(x=230, y=375)

bt = Button(i, width="20", text='dividir', command=bt_click3)
bt.place(x=230, y=450)

ed1 = Entry()
ed1.place(x=230, y=125)

ed2 = Entry()
ed2.place(x=230, y=150)

i.mainloop()
