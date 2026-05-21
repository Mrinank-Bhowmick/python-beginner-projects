# === Blind Auction · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @Polqt.
# Note: the project's art.py logo is inlined below so this runs as a single
# self-contained file in the browser playground.

# ASCII-art logo (originally in art.py)
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# Display the logo
print(logo)

# Store bids and a flag to end the auction
bids = {}
bidding_finished = False


# Find and announce the highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # Compare each bid to find the maximum
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


# Collect bids until no more bidders remain
while not bidding_finished:
    # Ask for the current bidder's name and amount
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid

    # Decide whether to continue or reveal the winner
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        find_highest_bidder(bids)
        bidding_finished = True
    elif should_continue == "yes":
        print()
