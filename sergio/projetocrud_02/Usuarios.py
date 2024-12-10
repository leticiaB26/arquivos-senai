
import mysql.connector 
from banco import banco

class Usuarios(object):
    def __init__(self,idusuario=0,nome="",telefone="",email="",usuario="",senha=""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco = banco()
        try:
          c = banco.conexao.cursor()
          c.execute("INSERT INTO usuario(nome,telefone,email,usuario,senha)VALUES(%s,%s,%s,%s,%s)",
                            (self.nome,self.telefone,self.email,self.usuario,self.senha))
          banco.conexao.commit()
          c.close()
          return "Usuario cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção de usuários: {e}"
        

    def alterarUsuario(self, id_usuario):
        banco = banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            UPDATE usuario
            SET nome = %s, telefone = %s, email = %s, usuario = %s, senha = %s
            WHERE id = %s
            """, (self.nome, self.telefone, self.email, self.usuario, self.senha, id_usuario))

            banco.conexao.commit()
            c.close()
            return "Usuário alterado com sucesso!"
            except Exception as e:
            return f"Ocorreu um erro ao alterar o usuário: {e}"