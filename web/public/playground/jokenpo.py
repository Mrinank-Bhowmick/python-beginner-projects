# === Jokenpo (Rock, Paper, Scissors) · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @jrbublitz.
# Note: the project's Jogadores and Partida classes are inlined below so this
# runs as a single self-contained file in the browser playground.

from random import randint


# A player: holds a name and a hand of cards (1=stone, 2=paper, 3=scissors)
class Jogadores:
    nome: str
    cartas = []

    def __init__(self, nome):
        self.nome = nome
        self.cartas = []

    # Deal three random cards to this player
    def distribuir_cartas(self) -> list:
        for i in range(3):
            carta = randint(1, 3)
            self.cartas.append(carta)
        return self.cartas

    # Turn card numbers into readable words
    def traduzir_cartas(self, cartas) -> list:
        cartasTraduzidas = ""
        for i in cartas:
            if i == 1 or i == "1":
                cartasTraduzidas += "Stone "
            elif i == 2 or i == "2":
                cartasTraduzidas += "Paper "
            else:
                cartasTraduzidas += "Scissors "

        return cartasTraduzidas

    # Empty this player's hand
    def limpar_cartas(self):
        return self.cartas.clear()


# A match between two players
class Partida(Jogadores):
    def __init__(self, jogador_um, jogador_dois):
        self.jogador_um = jogador_um
        self.jogador_dois = jogador_dois

    # Play an interactive match where you pick your cards
    def jogar(self):
        rodadas = []
        count_jogador1 = 0
        count_jogador2 = 0

        # Play two rounds
        for i in range(2):
            print("Suas Cartas: ", self.traduzir_cartas(self.jogador_um.cartas))
            carta_jogador1 = int(input("Escolha sua carta: "))

            # Computer picks a random card
            carta_jogador2 = randint(0, len(self.jogador_dois.cartas) - 1)

            # Record this round
            rodadas.append(
                self.traduzir_cartas(str(self.jogador_um.cartas[carta_jogador1]))
                + " x "
                + self.traduzir_cartas(str(self.jogador_dois.cartas[carta_jogador2]))
            )
            for rodada in rodadas:
                print(rodada)

            # Decide the round winner
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

            # Discard the cards that were played
            self.jogador_um.cartas.pop(carta_jogador1)
            self.jogador_dois.cartas.pop(carta_jogador2)

        # Announce the overall winner
        if count_jogador1 == count_jogador2:
            return print("Empate ")
        elif count_jogador1 > count_jogador2:
            return print("Jogador 1 - Venceu")
        return print("Jogador 2 - Venceu")

    # Play an automatic match using the dealt cards
    def simular(self):
        count_jogador1 = 0
        count_jogador2 = 0
        count_Empate = 0

        # Compare both hands card by card
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

        # Announce the overall winner
        if count_jogador1 == count_jogador2:
            return print("Empate ")

        if count_jogador1 > count_jogador2:
            return print("Jogador 1 - Venceu")
        return print("Jogador 2 - Venceu")


# Define a function to play interactively
def jogar():
    print("====== JOGAR ======")
    try:
        # Set up the human player
        jogador1 = Jogadores
        jogador1.nome = input("Digite seu nome: ")
        jogador1.distribuir_cartas(jogador1)

        # Set up the computer player
        jogador2 = Jogadores("Computador")
        jogador2.distribuir_cartas()

        # Start and run the match
        partida = Partida(jogador1, jogador2)
        partida.jogar()
    except Exception as e:
        print("Erro: " + str(e))


# Define a function to simulate a game automatically
def simularJogo():
    print("====== SIMULAÇÃO ======")
    try:
        # Create first simulated player and deal cards
        jogador1 = Jogadores("João")
        jogador1.distribuir_cartas()
        print(jogador1.nome, " - Cartas: ", jogador1.traduzir_cartas(jogador1.cartas))

        # Create second simulated player and deal cards
        jogador2 = Jogadores("Maria")
        jogador2.distribuir_cartas()
        print(jogador2.nome, " - Cartas: ", jogador2.traduzir_cartas(jogador2.cartas))

        # Run the simulation
        partida = Partida(jogador1, jogador2)
        partida.simular()
    except Exception as e:
        print("Erro: " + str(e))


# Show the menu and get the user's choice
print("Escolha um opção:\n" "1 - Jogar\n" "2 - Simular um jogo\n" "0 - Sair\n")
menu = int(input("Digite: "))

# Route to the right function based on choice
if menu == 1:
    jogar()
elif menu == 2:
    simularJogo()
else:
    print("Finalizando jogo...")
