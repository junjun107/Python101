#Todo1: Ask user for inputs
# name = input("What's your name?: ")

#Todo2: Save input data into a dic
# price = int(input("Enter your bid: "))


# bids[name] = price

#Todo3: Need add new bids?
# should_continue = input("Adding more bids? y or n")

#loop over dict
# Todo4: Compare for highests

import art

def find_highest_bidder(bidding_dict):
  winner = ""
  highest_bid = 0

  max(bidding_dict)

  for bidder in bidding_dict:
    bid_amount = bidding_dict[bidder]
    if bid_amount > highest_bid:
      highest_bid= bid_amount
      winner = bidder
  print(f"The winnder is ${winner} with a bid of ${highest_bid}")
bids= {}

continue_bidding = True

while continue_bidding:
  name = input("What's your name?: ")
  price = int(input("Enter your bid: "))
  bids[name] = price
  should_continue = input("Adding more bids? y or n").lower()
  if should_continue == 'n':
    continue_bidding = False
    find_highest_bidder(bids)
  elif should_continue == "y":
    print("\n" * 20)


print(art.logo)

