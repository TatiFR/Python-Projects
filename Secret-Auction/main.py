# 1. Show logo from art
from art import logo 
from replit import clear
print(logo)
    
# INSIDE def 2. Ask for name input   
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
    print(f"The winner is {winner} with a winning bid of ${highest_bid}")

while not bidding_finished: 
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ") 
    price = int(input("What's your bid?: $"))  
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == "No" or should_continue == "no":
       bidding_finished = True
       find_highest_bidder(bids)
    elif should_continue == "Yes" or should_continue == "yes" :
       clear()
