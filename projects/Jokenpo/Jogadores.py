# 1 = stone
# 2 = paper
# 3 = Scissors

from random import randint


class Jogadores:
    nome: str
    cartas = []

    def __init__(self, nome):  # Constructor
        self.nome = nome
        self.cartas = []

    # Return a list of cards
    def distribuir_cartas(self) -> list:
        for i in range(3):
            carta = randint(1, 3)
            self.cartas.append(carta)
        return self.cartas

    # Translate to letters
    def traduzir_cartas(self, cartas) -> list:
        cartasTraduzidas = ""
        for i in cartas:
            if i == 1 or i == "1":
                cartasTraduzidas += "Stone "  # Translated letters.append("Stone")
            elif i == 2 or i == "2":
                cartasTraduzidas += "Paper "  # Translated letters.append("Paper")
            else:
                cartasTraduzidas += "Scissors "  # Translated letters.append("Scissors")

        return cartasTraduzidas

    # Clear list
    def limpar_cartas(self):
        return self.cartas.clear()
