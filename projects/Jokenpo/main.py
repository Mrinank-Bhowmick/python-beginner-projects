from Partida import Partida
from Jogadores import Jogadores


def jogar():
    print("====== JOGAR ======")
    try:
        jogador1 = Jogadores
        jogador1.nome = input("Digite seu nome: ")
        jogador1.distribuir_cartas(jogador1)

        jogador2 = Jogadores("Computador")
        jogador2.distribuir_cartas()

        partida = Partida(jogador1, jogador2)
        partida.jogar()
    except Exception as e:
        print("Erro: " + str(e))


def simularJogo():
    print("====== SIMULAÇÃO ======")
    try:
        jogador1 = Jogadores("João")
        jogador1.distribuir_cartas()
        print(jogador1.nome, " - Cartas: ", jogador1.traduzir_cartas(jogador1.cartas))

        jogador2 = Jogadores("Maria")
        jogador2.distribuir_cartas()
        print(jogador2.nome, " - Cartas: ", jogador2.traduzir_cartas(jogador2.cartas))

        partida = Partida(jogador1, jogador2)
        partida.simular()
    except Exception as e:
        print("Erro: " + str(e))


print("Escolha um opção:\n" "1 - Jogar\n" "2 - Simular um jogo\n" "0 - Sair\n")
menu = int(input("Digite: "))

if menu == 1:
    jogar()
elif menu == 2:
    simularJogo()
else:
    print("Finalizando jogo...")
