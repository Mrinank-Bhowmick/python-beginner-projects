# === Blind Auction · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @yogesh78026.
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

# Display the logo and welcome message
print(logo)
print("Welcome to Blind Auction")

# Store all bids and a flag to end bidding
bids = {}
is_game_finished = False


# Find and print the highest bidder
def compare(bidding_record):
    highest_bidder = 0
    winner = " "
    # Loop through all bids to find the max
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the highest bid of {highest_bidder}.")


# Keep collecting bids until no bidders remain
while not is_game_finished:
    # Get this bidder's name and amount
    name = input("Enter your name: ")
    bidding_amount = int(input("Enter your bidding amount: "))
    bids[name] = bidding_amount

    # Check if more bidders need to go
    should_continue = input("Are there any other bidders? Type 'yes' or 'no':")
    if should_continue == "no":
        is_game_finished = True
        # Reveal the winner when bidding ends
        compare(bids)
    elif should_continue == "yes":
        print("Continue bidding")
        # clear()
