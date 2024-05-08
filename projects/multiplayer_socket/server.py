from socket import *
from _thread import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverName = ""
serverPort = 12000  # same port as given in client.py
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
attributes = {}
thread = 0
score = [0, 0]


def init_server():  # initialise server for new game
    attributes["chooser"] = ""
    attributes["guesser"] = ""
    attributes["guess_message"] = ""
    attributes["guess_ans"] = ""
    attributes["guessed"] = 0
    attributes["checked"] = 1
    attributes["break1"] = 0
    attributes["break2"] = 0
    attributes["rps"] = ["", "1"]
    attributes["rps_count"] = 0
    attributes["player1"] = ""
    attributes["player2"] = ""
    attributes["mes"] = ""


print("Server ready")


def game1_guesser(clientAddress):
    while not attributes["break1"]:
        if attributes["checked"]:
            attributes["guesser"].send(
                "Enter your guess".encode()
            )  # send prompt to guess word
            print("Enter the guess")
            attributes["guess_message"] = (
                attributes["guesser"].recv(2048).decode().upper()
            )  # receive guess
            print("guess_message", attributes["guess_message"])
            attributes["chooser"].send(
                attributes["guess_message"].encode()
            )  # send guess to other player
            print("guess sent to chooser")
        if attributes["guess_message"] != "":
            attributes["guessed"] = 1
            attributes["checked"] = 0
            attributes["guess_message"] = ""


def game1_chooser(clientAddress, word):
    clue = 0
    while True:
        attributes["guess_ans"] = (
            attributes["chooser"].recv(2048).decode().upper()
        )  # **a**r(or win/lose),count
        if not attributes["guess_ans"]:
            continue
        print("Got guess ans")
        attributes["guess_ans"], count = attributes["guess_ans"].split(":")
        attributes["guesser"].send(
            attributes["guess_ans"].encode()
        )  # send guess result to player
        print("sent guess answer to guesser", count)
        if (
            "won" in attributes["guess_ans"].lower()
            or "lost" in attributes["guess_ans"].lower()
        ):
            attributes["break1"] = 1
            break
        if count == "3" and clue == 0:
            clue = 1
            attributes["chooser"].send(
                "Enter the clue".encode()
            )  # prompt player for clue
            clue = (
                "Clue=" + attributes["chooser"].recv(2048).decode().upper()
            )  # receive clue
            print("clue", clue)
            attributes["guesser"].send(clue.encode())  # send clue to other player
        if attributes["guess_ans"] != "":
            attributes["guessed"] = 0
            attributes["checked"] = 1
            attributes["guess_ans"] = ""


def pre_game1(clientSocket, clientAddress):
    print("hangman")
    while True:
        if attributes["chooser"] == "":
            attributes["mes"] = "Get ready to play hangman\nChoose a word\n"
            attributes["chooser"] = clientSocket
            attributes["chooser"].send(attributes["mes"].encode())
            word = (
                attributes["chooser"].recv(2048).decode().upper()
            )  # receive chosen word from player
            print("Chosen word=", word)
            game1_chooser(clientAddress, word)  # call subroutine for chooser
            break
        else:
            attributes["mes"] = (
                "Get ready to play hangman\nYou will be guessing the  word\n"
            )
            attributes["guesser"] = clientSocket
            attributes["guesser"].send(attributes["mes"].encode())
            game1_guesser(clientAddress)  # call subroutine for guesser
            break


def decision():  # function to calculate score for rock,paper and scissors
    attributes["rps_count"] += 1
    rps = attributes["rps"]
    if rps[0] == "ROCK":
        p1 = 0
    if rps[0] == "PAPER":
        p1 = 5
    if rps[0] == "SCISSOR":
        p1 = 2
    if rps[1] == "ROCK":
        p2 = 0
    if rps[1] == "PAPER":
        p2 = 5
    if rps[1] == "SCISSOR":
        p2 = 2
    if p1 == 0:
        if p2 == 0:
            return -1
        elif p2 == 2:
            return 1
        else:
            return 2
    if p1 == 2:
        if p2 == 0:
            return 2
        elif p2 == 5:
            return 1
        else:
            return -1
    if p1 == 5:
        if p2 == 0:
            return 1
        elif p2 == 2:
            return 2
        else:
            return -1


def game2_1(clientAddress):
    while not attributes["break2"]:
        if attributes["mes"] == "":
            attributes["player1"].send(
                "Play".encode()
            )  # send prompt to player1 to play
            attributes["mes"] = (
                attributes["player1"].recv(2048).decode().upper()
            )  # receive player 1's choice
            attributes["rps"][0] = attributes["mes"]


def game2_2(clientAddress):
    while not attributes["break2"]:
        if attributes["mes"] != "":
            attributes["player2"].send(
                "Play".encode()
            )  # send prompt to player2 to play
            attributes["mes"] = (
                attributes["player2"].recv(2048).decode().upper()
            )  # receive player 2's choice
            attributes["rps"][1] = attributes["mes"]
            ans = decision()  # check decision
            if ans != -1:
                score[ans - 1] += 1  # update score
            if attributes["rps_count"] == 3:  # set result when 3 tries done
                if score[0] > score[1]:
                    attributes["mes"] = "Player 1 won"
                elif score[0] < score[1]:
                    attributes["mes"] = "Player 2 won"
                else:
                    attributes["mes"] = "Draw"
                attributes["break2"] = 1
            else:
                attributes["mes"] = ",".join(attributes["rps"]) + ",".join(
                    map(str, score)
                )
            attributes["player1"].send(
                attributes["mes"].encode()
            )  # send result to player1
            attributes["player2"].send(
                attributes["mes"].encode()
            )  # send result to player2
            attributes["mes"] = ""


def pre_game2(clientSocket, clientAddress):
    print("Rock, Paper, Scissor")
    while True:
        if attributes["player1"] == "":  # give first user as player1
            attributes["player1"] = clientSocket
            print(attributes["player1"])
            attributes["player1"].send(
                "Get ready to play Rock, Paper, Scissor\nYou are Player 1".encode()
            )
            game2_1(clientAddress)
            break
        else:  # next player as player2
            attributes["player2"] = clientSocket
            attributes["player2"].send(
                "Get ready to play Rock, Paper, Scissor\nYou are Player 2".encode()
            )
            game2_2(clientAddress)
            break


def multi_client(clientSocket, clientAddress):
    while True:
        choice = clientSocket.recv(2048).decode()
        print(clientAddress, "chose", choice)
        if choice == "1":
            pre_game1(clientSocket, clientAddress)
            break
        elif choice == "2":
            pre_game2(clientSocket, clientAddress)
            break
        choice = 0
        clientSocket.close()


while True:
    (
        connectionSocket,
        clientAddress,
    ) = serverSocket.accept()  # welcome socket accepts new client
    print("Connected to: " + clientAddress[0])
    start_new_thread(
        multi_client,
        (
            connectionSocket,
            clientAddress,
        ),
    )  # a thread created for each user
    thread += 1
    print("Client number connected: ", thread)
    if thread % 2 == 1:
        init_server()  # restart server for every game

serverSocket.close()
