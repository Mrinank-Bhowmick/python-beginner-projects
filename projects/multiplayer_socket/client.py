from socket import *

serverName = "server ip"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)  # create TCP socket
clientSocket.connect((serverName, serverPort))


def game1_chooser():  # player choosing the word for hangman
    close = 0
    word = input()
    ans = ["*"] * len(word)
    count = 0
    clientSocket.send(word.encode())  # send the chosen word to server
    print("Word sent to server")
    while True:
        guess = ""
        print("Waiting for guess...")
        guess = (
            clientSocket.recv(2048).decode().upper()
        )  # receive the guess given by player guessing it
        print("Guess=", guess)
        if "clue" in guess.lower():
            print(guess)
            clue = input()
            clientSocket.send(clue.encode())  # send clue to server
            continue
        flag = 0
        pos = input("Enter the positions of occurances\n").split()
        if "-1" not in pos:
            for x in range(len(pos)):
                ans[int(pos[x]) - 1] = guess  # set the value at correct position
                flag = 1
        if flag == 0:
            count += 1
        if count == 7 and "*" in ans:  # end game after 7 guesses
            mes = "You lost...The word is " + word + ":" + str(count)
            close = 1
        elif count < 7 and "*" not in ans:  # end game if all characters guessed
            mes = "You won...The word is " + word + ":" + str(count)
            close = 1
        else:
            mes = "".join(ans) + ":" + str(count)
        clientSocket.send(mes.encode())  # send the result to server
        if close:
            break


def game1_guesser():  # player guessing word in hangman
    while True:
        mes = clientSocket.recv(2048).decode()  # receive enter prompt from server
        if "Enter" in mes:
            guess = input(mes)
            print("Guessing done...")
            clientSocket.send(guess.encode())  # send guess to server
            print("Guess sent to server")
            guess_res = clientSocket.recv(2048).decode()  # receive result from server
            if (
                "won" in guess_res.lower() or "lost" in guess_res.lower()
            ):  # if result has won or lost display it and end game by closing socket
                print(guess_res)
                clientSocket.close()
                break
            else:
                print(guess_res)
        if "clue" in mes.lower():
            print(mes)


def game2():  # Rock, paper, scissor game
    while True:
        mes = clientSocket.recv(2048).decode()  # Receive 'play' prompt from server
        if mes == "Play":
            print(mes)
            inp = input().upper()
            while (
                inp != "ROCK" and inp != "PAPER" and inp != "SCISSOR"
            ):  # retry if wrong input
                inp = input("Choose between rock, paper or scissor\n").upper()
            clientSocket.send(inp.encode())  # send choice to server
            rps_score = clientSocket.recv(2048).decode()  # receive score from server
            if (
                "won" in rps_score.lower() or "draw" in rps_score.lower()
            ):  # end game by closing socket
                print(rps_score)
                clientSocket.close()
                break
            else:
                print(rps_score)


while True:
    print("Enter your choice(1 or 2)")  # choice to choose which game
    choice = input()
    clientSocket.send(choice.encode())  # send choice to server
    choice = clientSocket.recv(2048).decode()  # receive acknowledgement from server
    print(choice)
    if "hangman" in choice.lower():
        if "choose" in choice.lower():
            game1_chooser()
            break
        if "guess" in choice.lower():
            game1_guesser()
            break
    if "rock" in choice.lower():
        game2()
        break
