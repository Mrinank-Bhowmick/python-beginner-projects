from random import randint
from Jogadores import Jogadores


class Partida(Jogadores):
    def __init__(self, jogador_um, jogador_dois):  # Constructor
        self.jogador_um = jogador_um
        self.jogador_dois = jogador_dois

    def jogar(self):
        rodadas = []
        count_jogador1 = 0
        count_jogador2 = 0

        for i in range(2):
            print("Suas Cartas: ", self.traduzir_cartas(self.jogador_um.cartas))
            carta_jogador1 = int(input("Escolha sua carta: "))
            # print(self.traduzir_cartas(self.jogador_um.cartas[carta_jogador1]))

            carta_jogador2 = randint(0, len(self.jogador_dois.cartas) - 1)
            # print(self.traduzir_cartas(self.jogador_dois.cartas[carta_jogador2]))

            rodadas.append(
                self.traduzir_cartas(str(self.jogador_um.cartas[carta_jogador1]))
                + " x "
                + self.traduzir_cartas(str(self.jogador_dois.cartas[carta_jogador2]))
            )
            for rodada in rodadas:
                print(rodada)

            # Game rule
            if self.jogador_um.cartas[carta_jogador1] == 1:
                if self.jogador_dois.cartas[carta_jogador2] == 2:
                    count_jogador2 += 1
                else:
                    count_jogador1 += 1
            if self.jogador_um.cartas[carta_jogador1] == 2:
                if self.jogador_dois.cartas[carta_jogador2] == 3:
                    count_jogador2 += 1
                else:
                    count_jogador1 += 1

            if self.jogador_um.cartas[carta_jogador1] == 3:
                if self.jogador_dois.cartas[carta_jogador2] == 1:
                    count_jogador2 += 1
                else:
                    count_jogador1 += 1

            # Remove the selected ones
            self.jogador_um.cartas.pop(carta_jogador1)
            self.jogador_dois.cartas.pop(carta_jogador2)

        if count_jogador1 == count_jogador2:
            return print("Empate ")
        elif count_jogador1 > count_jogador2:
            return print("Jogador 1 - Venceu")
        return print("Jogador 2 - Venceu")

    # Method to start the game
    def simular(self):
        count_jogador1 = 0
        count_jogador2 = 0
        count_Empate = 0

        for round in range(3):
            if self.jogador_um.cartas[round] == self.jogador_dois.cartas[round]:
                print("Round(" + str(round + 1) + ") - Empate")
                count_Empate += 1
                if count_Empate == 3:
                    return print("Todos os rounds Empataram !")
            else:
                if self.jogador_um.cartas[round] == 1:
                    if self.jogador_dois.cartas[round] == 2:
                        count_jogador2 += 1
                    else:
                        count_jogador1 += 1

                if self.jogador_um.cartas[round] == 2:
                    if self.jogador_dois.cartas[round] == 3:
                        count_jogador2 += 1
                    else:
                        count_jogador1 += 1

                if self.jogador_um.cartas[round] == 3:
                    if self.jogador_dois.cartas[round] == 1:
                        count_jogador2 += 1
                    else:
                        count_jogador1 += 1

        if count_jogador1 == count_jogador2:
            return print("Empate ")

        if count_jogador1 > count_jogador2:
            return print("Jogador 1 - Venceu")
        return print("Jogador 2 - Venceu")
