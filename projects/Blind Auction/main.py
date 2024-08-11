from replit import clear

# HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while not bidding_finished:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        find_highest_bidder(bids)
        bidding_finished = True
    elif should_continue == "yes":
        clear()
