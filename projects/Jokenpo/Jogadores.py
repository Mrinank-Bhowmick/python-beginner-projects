# 1 = Pedra
# 2 = Papel
# 3 = Tesoura

from random import randint

class Jogadores:
    nome: str
    cartas = []

    def __init__(self, nome): # Construtor da classe
            self.nome = nome
            self.cartas = []

    def distribuir_cartas(self) -> list: # Retorno uma lista com as cartas
        for i in range(3):
             carta = randint(1, 3)
             self.cartas.append(carta)
        return self.cartas

    def traduzir_cartas(self, cartas) -> list: # Traduz a cartas
        cartasTraduzidas = ""
        for i in cartas:
            if i == 1 or i == "1":
                # cartasTraduzidas.append("Pedra")
                cartasTraduzidas += "Pedra "
            elif i == 2 or i == "2":
                # cartasTraduzidas.append("Papel")
                cartasTraduzidas += "Papel "
            else:
               # cartasTraduzidas.append("Tesoura")
               cartasTraduzidas += "Tesoura "

        return cartasTraduzidas

    def limpar_cartas(self): # Limpa lista
        return self.cartas.clear()