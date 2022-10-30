from distutils.command.install_scripts import install_scripts
# from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to Blind Auction")

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bidder = 0
#   winner = " "
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bidder:
#       highest_bidder = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bidder}")

# while not bidding_finished:
#   name = input("Enter your name: ")
#   bidding = int(input("What is your bidding price: $"))
#   bids[name] = bidding
#   should_continue = input("Are there any other bidders. Type 'Yes' or 'No'")
#   if should_continue == "No":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "Yes":
#     clear()



bids = {}
is_game_finished = False

def compare(bidding_record):
  highest_bidder = 0
  winner = " "
  for bidder in bidding_record:
    bid_amount = bidding_record[bidding_record]
    if bid_amount > highest_bidder:
      highest_bidder = bid_amount
      winner = bidder
    print(f"The winner is {bidder} with the highest bid of {highest_bidder}. ")


while not is_game_finished:
  name = input("Enter your name: ")
  bidding_amount = int(input("Enter your bidding amount: "))
  bids[name] = bidding_amount

  should_continue = input("Are there any other bider? Type 'yes' or 'no' :")
  if should_continue == 'no':
    is_game_finished = True
    compare(bids)
  elif should_continue == 'yes':
    print("continue bidding")
    # clear()

