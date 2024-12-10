from tkinter import *

def bt_click():
    try:
        peso = float(peso1.get())
        altura = float(altura1.get()) / 100  
        imc = peso / (altura ** 2)  
        resultado_lb["text"] = f"IMC: {imc:.2f}"  
    except ValueError:
        resultado_lb["text"] = "Insira valores válidos!"  


i = Tk()
i.title("Programa IMC")
i.geometry("800x600+250+30")
i.wm_iconbitmap('icone.ico')

i["bg"] = "grey"


resultado_lb = Label(i, text='IMC: 0.00')
resultado_lb.place(x=230, y=200)


Label(i, text='Peso (kg)').place(x=150, y=123)
Label(i, text='Altura (cm)').place(x=140, y=150)


Label(i, text='Aluna: Leticia Da Veiga').place(x=100, y=95)


bt = Button(i, width=20, text='Calcular', command=bt_click)
bt.place(x=230, y=230)


peso1 = Entry(i)
peso1.place(x=230, y=125)

altura1 = Entry(i)
altura1.place(x=230, y=150)

i.mainloop()
