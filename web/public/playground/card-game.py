# === Card Game - War · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @Sayakb03.

from random import shuffle
import re


# Define a single playing card with value and suit
class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [
        None,
        None,
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    # Store the card's value and suit as integers
    def __init__(self, v, s):
        self.value = v
        self.suit = s

    # Compare this card as less than another
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    # Compare this card as greater than another
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    # Return a human-readable card name
    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v


# Build and shuffle a full 52-card deck
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    # Remove and return the top card
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


# Represent a player with a name and win count
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


# Manage the overall War game logic
class Game:
    # Ask for player names and set up the deck
    def __init__(self):
        while True:
            pattern = r"\W"
            name1 = input("Player 1 name: ")
            name2 = input("Player 2 name: ")
            str = name1 + name2
            if re.search(pattern, str) == None:
                break
            else:
                print("Please, don't use special characters")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    # Print which player won this round
    def display_winner(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    # Print what each player drew
    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    # Run the main game loop round by round
    def play_game(self):
        cards = self.deck.cards
        print("Beginning War!")
        while len(cards) >= 2:
            m = "q to quit. Any " + "key to play:"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.display_winner(self.p1.name)
            else:
                self.p2.wins += 1
                self.display_winner(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("War is over. {} wins".format(win))

    # Determine the overall game winner
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"


# Create and start the game
game = Game()
game.play_game()
