
from Usuarios import Usuarios
from tkinter import *
import mysql.connector


class Application:

    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        # ///////////////////////
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        # ///////////////////////
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        # ///////////////////////
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        # ///////////////////////
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        # ///////////////////////
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        # ///////////////////////
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        # ///////////////////////
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        # ///////////////////////
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        # LABEL

        self.titulo = Label(self.container1, text="informe os dados: ")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblidusuario = Label(
            self.container2, text="idUsuario", font=self.font, width=10)
        self.lblidusuario.pack(side=LEFT)

        # caixa de texto

        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte

        self.txtusuario = Entry(self.container6)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = label(
            self.container7, text="senha:", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)
        Self.textsenha = Entry(self.container7)
        self.textsenha["width"] = 25
        self.textsenha["show"] = "*"
        self.text["font"] = self.fonte
        self.textsenha.pack(side=LEFT)

        self.btnInsert = Button(
            self.container8, text="inserir", font=self.fonte, width=12)
        self.btnInsert["command"] = self.inseriUsuario
        self.btnInsert.pack(side=LEFT)

        self.bntAlterar = Button(
            self.container8, text="alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterariUsuario
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(
            self.container8, text="excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.exluiriUsuario
        self.bntExcluir.pack(side=LEFT)

        self.bntLimpar = Button(
            self.container8, text="limpar", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.limpariUsuario
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg =label(self.container9, text="")
        self.lblmsg["font"] = ("verdana", "9", "italic")
        self.lblmsg.pack()

        self.conectarBanco()

    def conectarBanco(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            databsase="leticia_db"
        )
        self.cursor = self.conn.cursor()
        self.cursor = execute('''CREATE TABLE IF NOT EXISTS tb_usuario  INT AUTO INCREMENT PRIMARY KEY',nome VARCHAR(255),
        telefone VARCHAR(255),
        email VARCHAR(255)
        usuario VARCHAR(255),
        senha VARCHAR(255))''')

        self.conn.commit()

    def inserirUsuario(self):
        nome = self.txtnome.get()
        telefone = self.txttelefone.get()
        email = self.txtemail.get()
        usuario = self.txtusuario.get()
        senha = self.txtsenha.get()
        self.cursor.execute("INSERT INTO tb_usuario(nome,telefone,email,usuario,senha)VALUES(%s,%s,%s,%s,%s)",
                            (nome, telefone, email, usuario, senha))

        self.conn.commit()
        self.lblmsg["text"] = "usuario inserido com sucesso"
        self.limparCampos()

        def alterarusuario(self):

            nome = self.txtnome.uppdate()
            telefone = self.txttelefone.uppdate()
            email = self.txtemail.uppdate()
            usuario = self.txtusuario.uppdate()
            senha = self.txtsenha.uppdate()
            self.cursor.execute("UPPDATE FROM tb_usuario WHERE(nome,telefone,email,usuario,senha)VALUES(%s,%s,%s,%s,%s)",
                                (nome, telefone, email, usuario, senha))

            self.conn.commit()
            self.lblmsg["text"] = "usuario alterado com sucesso"
            self.limparCampos()

    def excluirusuario(self):
        idUsuario = self.txtidusuario.get()
        self.cursor.execute(
            "DELE FROM tb_usuario WHRE idUsuario=%s", (idUsuario,))
        self.conn.commit()
        self.lblmsg["text"] = "usuario excluido com sucesso"
        self.limparCampos()

    def buscarUsuario(self):
        idUsuario = self.txtidusuario.get()
        self.cursor.execute(
            "SELCT * FROM tb_usuario WHERE idUsuario=%s", (idUsuario,))
        usuario = self.cursorfetchone()

        if usuario:
            self.txtnome.insert(0, usuario[1])
            self.txttelefone.insert(0, usuario[2])
            self.txtemail.insert(0, usuario[3])
            self.txtusuario.insert(0, usuario[4])
            self.txtsenha.insert(0, usuario[5])
        else:
            self.lblmsg["text"] = "usuario não encontrado"
            self.limpaCampos

    def limpaCampos(self):
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    def __del__(self):
        self.conn.close


if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()
