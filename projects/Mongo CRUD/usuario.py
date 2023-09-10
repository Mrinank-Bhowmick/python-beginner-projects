from conexao import db
import pandas as pd

# from bson.objectid import ObjectId


class Usuario:
    # CONSTRUCTOR CLASS USER
    def __init__(self, nome="", cpf="", idade=0, altura=0):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.altura = altura
        self.usuarios = db["usuarios"]

    # INSERT REGISTER
    def inserir_um_registro(self):
        if not self.existe_registro(self.cpf):
            dados_usuario = dict(
                nome=self.nome, cpf=self.cpf, idade=self.idade, altura=self.altura
            )
            self.usuarios.insert_one(dados_usuario)
        else:
            raise Exception("Registro já existe !")

    # FIND REGISTERS
    def pesquisa_registro(self, cpf=""):
        if cpf != "":
            user = self.usuarios.find({"cpf": cpf}, {"_id": 0})[0]
            return user
        else:
            print(f"{' Listagem de usuários ':=^40}")
            print(pd.DataFrame(self.usuarios.find({"cpf": self.cpf}, {"_id": 0})))

    # CHANGE REGISTERS
    def alterar_registro(self, cpf):
        usuario = self.pesquisa_registro(cpf)

        if self.nome != "":
            usuario["nome"] = self.nome
        if self.cpf != "":
            usuario["cpf"] = self.cpf
        if self.idade != 0:
            usuario["idade"] = self.idade
        if self.altura != 0:
            usuario["altura"] = self.altura

        if not self.existe_registro(self.cpf):
            db.usuarios.update_one({"cpf": cpf}, {"$set": usuario})
        else:
            raise Exception("CPF já existente !")

    # LIST ALL REGISTERS
    def listar_registros(self):
        print(f"{' Listagem de usuários ':=^40}")
        print(pd.DataFrame(self.usuarios.find({}, {"_id": 0})))

    # VERIFY IF REGISTER EXIST ON DB
    def existe_registro(self, cpf) -> bool:
        dados = dict(cpf=cpf)
        if self.usuarios.find(dados).count() > 0:
            return True
        return False

    # CLEAN SPECIFIC REGISTER DB
    def deletar_registro(self, cpf):
        self.usuarios.find_one_and_delete({"cpf": cpf})
        # self.usuarios.delete_one({"_id":ObjectId("607f020ee2dd4f554c912cd3")}) # Objects ID

    # CLEAN ALL REGISTER DB
    def limpar_banco(self):
        self.usuarios.delete_many({})


# Testing methods

user = Usuario("Bruno", "", 25, 1.30)
# user.limpar_banco()
# user.inserir_um_registro()
user.alterar_registro("022")
# user.listar_registros()
# user.pesquisa_registro()
# user.deletar_registro("01234")
