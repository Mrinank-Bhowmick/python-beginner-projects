# === BLACKJACK · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @ChiragAgg5k.

# Import random for shuffling
import random

# Define card suits, ranks, and point values
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}
# Track player chips and game state
chips = 100
game_num = 0
game_on = True


# Represent a single playing card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# Represent a full 52-card deck
class Deck:
    def __init__(self):
        self.all_cards = []
        # Build every suit-rank combination
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Remove and return the top card
        return self.all_cards.pop()


# Let the player choose Ace value (1 or 11)
def check_ace(card):
    if card.rank == "Ace":
        while True:
            ace_val = int(
                input("\nWhat value do you want to consider for Ace (1/11)? :")
            )

            if ace_val == 1:
                values["Ace"] = 1

                break
            elif ace_val == 11:
                values["Ace"] = 11

                break
            else:
                print("choose valid value.")
                continue


# Clear the terminal and show the title banner
print("\n" * 100)

print(
    """
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝"""
)

# Print game rules for the player
print(
    """
BlackJack is very popular card game mainly played in casinos around the world.
Let's imagine this program as a virtual casino with computer as the Dealer.
The purpose of this game is to beat the Dealer, which can be done in various ways.

---------------------------------------------------------------------------------------------------------------
Both the player and the dealer are given 2 cards at the beginning , but one of the dealer's card is kept hidden.

Each card holds a certain value.
Numbered cards contain value identical to their number.
All face cards hold a value of 10
Ace can either hold a value of 1 or 11 depending on the situation.

BlackJack means 21. Whoever gets a total value of 21 with their cards immediately wins!
(winning through blackjack results in 3x the money)
If the value of cards goes over 21, it's called a BUST, which results in an immediate loss...
If both the players get the same value of cards , it's a TIE and the bet money is returned.

If none of the above cases are met ,the person with closer value to 21 wins.
(winning like this returns 2x the bet money)
---------------------------------------------------------------------------------------------------------------

Let the game begin!"""
)

# Main game loop — runs each round
while game_on:
    try:
        # Create and shuffle a fresh deck each round
        new_deck = Deck()
        new_deck.shuffle()

        game_num += 1
        print(f"\nGame Round number : {game_num}")
        print(f"Chips remaining = {chips}")

        # Ask player how many chips to bet
        while True:
            bet = int(input("\nEnter the amount of chips you want to bet:"))
            if bet > chips:
                print("You dont have enough chips.")
                print("Enter a valid amount. \n")
            elif bet <= 0:
                print("Invalid Bet")
            else:
                chips -= bet
                break

        # Deal two cards each to player and dealer
        player_table_cards = []
        dealer_table_cards = []

        [player_table_cards.append(new_deck.deal_one()) for i in range(2)]
        [dealer_table_cards.append(new_deck.deal_one()) for i in range(2)]

        # Show player cards; hide one dealer card
        print(f"\nPlayer cards are {player_table_cards[0]} and {player_table_cards[1]}")
        print(f"Dealer cards are {dealer_table_cards[0]} and Hidden.")

        # Check player's starting cards for Ace
        check_ace(player_table_cards[0])
        check_ace(player_table_cards[1])

        # Let the player hit or stand
        while True:
            hit_or_stand = input("Do you want to hit or stand? :").lower()

            if hit_or_stand == "hit":
                # Deal one more card to the player
                player_table_cards.append(new_deck.deal_one())
                check_ace(player_table_cards[-1])

                print(f"\nThe player hits card : {player_table_cards[-1]}")

                print("\nPlayer's hand :")
                [print(i) for i in player_table_cards]
                print()

                player_cards_val = 0

                for i in player_table_cards:
                    player_cards_val += i.value

                # Stop if player hits 21 or busts
                if player_cards_val == 21:
                    print("You got a blackjack!")
                    break

                elif player_cards_val < 21:
                    continue

                else:
                    print("YOU BUSTED!")
                    break

            elif hit_or_stand == "stand":
                # Calculate player total on stand
                player_cards_val = 0
                for i in player_table_cards:
                    player_cards_val += i.value

                print("\nPlayer has decided to stand.")

                print("\nPlayer's hand:")
                [print(i) for i in player_table_cards]
                print()

                if player_cards_val == 21:
                    print("Player got a blackjack!")
                    break

                break

            else:
                print("Enter a valid option. \n")
                continue

        # Dealer draws until reaching at least 17
        no_of_hits = 0

        while True:
            dealer_cards_val = 0

            # Recalculate dealer total each loop
            for i in dealer_table_cards:
                dealer_cards_val += i.value

            if dealer_cards_val < 17:
                no_of_hits += 1
                dealer_table_cards.append(new_deck.deal_one())
                continue

            elif 17 <= dealer_cards_val < 21:
                print(f"The Dealer has hit {no_of_hits} times.")
                print("\nDealer's hand :")
                [print(i) for i in dealer_table_cards]
                break

            elif dealer_cards_val == 21:
                print(f"The Dealer has hit {no_of_hits} times.")
                print("The Dealer got a blackjack!")
                print("\nDealer's hand :")
                [print(i) for i in dealer_table_cards]
                break

            elif dealer_cards_val > 21:
                # Dealer bust only counts if player didn't bust
                if not (player_cards_val > 21):
                    print(f"The Dealer has hit {no_of_hits} times.")
                    print("The Dealer busted!")
                    print("\nDealer's hand :")
                    [print(i) for i in dealer_table_cards]
                    break

                else:
                    break

        # Decide winner and update chips
        if player_cards_val > 21:
            print(
                "\nSince the Player busted , the round is lost.\nPlayer lost the bet money"
            )

        elif dealer_cards_val > 21:
            print(
                "\n Since the Dealer busted , Player won the round! \nPlayer got twice the money bet."
            )
            chips += bet * 2

        elif player_cards_val == 21:
            print("\nPlayer won with a blackjack! \nPlayer got thrice the money bet.")
            chips += bet * 3

        elif 21 - player_cards_val > 21 - dealer_cards_val:
            print("\nDealer won the round. \nPlayer lost the bet money")

        elif 21 - dealer_cards_val > 21 - player_cards_val:
            print("\nPlayer won the round. \nPlayer got twice the money bet.")
            chips += bet * 2

        else:
            # Equal distance to 21 means a tie
            print("\nIt's a tie. \nBet money was returned.")
            chips += bet

        # End game if player has no chips left
        if chips == 0:
            print("\nYou are out of chips , Game over.")
            break

        else:
            # Ask if the player wants another round
            cont = input("Do you want to continue? (y/n) :")
            check = cont.upper()

            if check == "Y":
                print("\n" * 100)

                print(
                    """
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝"""
                )

                continue

            else:
                print(f"\nTotal amount of chips left with the player = {chips}")
                print(input("Press Enter to exit the terminal..."))
                break

    except Exception as error:
        # Catch errors and retry the round
        print(f"Following error occurred : {error} \nPlease try again.")
        game_num -= 1
        continue
