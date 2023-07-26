# Importing the required module
from distutils.command.install_scripts import install_scripts

# Importing the logo from the 'art' module
from art import logo

# Display the logo and welcome message
print(logo)
print("Welcome to Blind Auction")

# Dictionary to store the bids and flag to indicate if bidding is finished
bids = {}
is_game_finished = False


# Function to compare the bids and find the highest bidder
def compare(bidding_record):
    highest_bidder = 0
    winner = " "
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the highest bid of {highest_bidder}.")


# Main loop for the bidding process
while not is_game_finished:
    name = input("Enter your name: ")
    bidding_amount = int(input("Enter your bidding amount: "))
    bids[name] = bidding_amount

    # Check if there are any other bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no':")
    if should_continue == "no":
        is_game_finished = True
        # Call the compare function to find the highest bidder and print the result
        compare(bids)
    elif should_continue == "yes":
        print("Continue bidding")
        # clear()
        # Here, the 'clear()' function is usually used to clear the console output,
        # but it's currently commented out in this code snippet.
