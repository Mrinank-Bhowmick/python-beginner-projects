# BLACKJACK

Blackjack is a very popular card game commonlu played in casinos worldwide.
This program will simulate a virtual casino, with computer as the dealer.
The purpose of this game is to beat the dealer, which can be done in various ways.

## Example

```text
Game Round number : 1
Chips remaining = 100

Enter the amount of chips you want to bet: 20

Player cards are Seven of Hearts and King of Spades
Dealer cards are Four of Clubs and Hidden.
Do you want to hit or stand? : hit

The player hits card : Three of Diamonds

Player's hand :
Seven of Hearts
King of Spades
Three of Diamonds

YOU BUSTED!
The Dealer has hit 2 times.
Dealer's hand :
Four of Clubs
Nine of Hearts
Five of Spades

Since the Player busted , the round is lost.
Player lost the bet money
Do you want to continue? (y/n) : n

Total amount of chips left with the player = 80
```

## Rules

- At the start of the game, both the player and the dealer are given 2 cards, however one of the dealer's card is kept hidden.
- Each card holds a certain value.
  - Numbered cards have a value identical to their number.
  - All face cards (e.g. King, Queen) hold a value of 10.
  - Aces can either hold a value of 1 or 11, depending on the situation.
- Blackjack refers to a total card value of **21**. When a player achieves this, they immediately win, and the victory results in a payout 3x the amount of the bet!
- If the total value of cards exceeds 21, it's called a BUST, which results in immediate loss. If both participants bust, the result is a tie, and the bets are returned.
- If none of the above conditions are met, the person with a closer value to 21 wins. Winning in this manner results in a payout 2x the amount of the bet!

-----------------------------------------------------------------------------------------------------------------

PLEASE NOTE: For simplicity, this program does not include advanced moves, such as double downs, splits and surrenders. The program also currently lacks proper linting, debugging and optimization.
