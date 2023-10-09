# BLACKJACK

Blackjack is a very popular card game commonlu played in casinos worldwide.
This program will simulate a virtual casino, with computer as the dealer.
The purpose of this game is to beat the dealer, which can be done in various ways.

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
