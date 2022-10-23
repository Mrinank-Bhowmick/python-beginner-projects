# BLACKJACK

BlackJack is very popular card game mainly played in casinos around the world.
Let's imagine this program as a virtual casino with computer as the **Dealer**.
The purpose of this game is to beat the Dealer, which can be done in various ways.

## Rules

- Both the player and the dealer are given 2 cards at the beginning , but one of the dealer's card is kept hidden.

Each card holds a certain value.

- Numbered cards contain value identical to their number.
- All face cards hold a value of 10
- Ace can either hold a value of 1 or 11 depending on the situation.

BlackJack means **21**. Whoever gets a total value of 21 with their cards immediately wins!
*(winning through blackjack results in 3x the money)*

If the value of cards goes over 21, its called a BUST, which results in immediate loss...
If both the players get the same value of cards , it's a TIE and the betted money is returned.

If none of the above cases are met ,the person with closer value to 21 wins.
*(winning like this returns 2x the betted money)*

-----------------------------------------------------------------------------------------------------------------

For simplicity of the program a lot of  moves like double down,split and surrender were skipped.
The program also lacks proper linting , debugging and optimization at the moment.
