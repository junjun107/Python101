#Todo1: Ask user for inputs
# name = input("What's your name?: ")

#Todo2: Save input data into a dic
# price = int(input("Enter your bid: "))


# bids[name] = price

#Todo3: Need add new bids?
# should_continue = input("Adding more bids? y or n")

#loop over dict
# Todo4: find out highests bids

#save data into a dictionary
#anymore bidders?
#use a while loop to continute bidding

def find_highest_bidder(bidding_dict): #function to find highest bidder, loop over object
  highest_bid = 0
  winner = ""
  for bidder in bidding_dict:
    bid_amount = bidding_dict[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount #find highest bid
      winner = bidder
  print(f"Winner is {winner} with bid: ${highest_bid}")

bids = {}

continue_bidding = True

while continue_bidding:
  name = input("Enter your name:")
  price = int(input("Enter your bid: "))
  bids[name] = price
  should_continue = input("Are there any more bidders? y or n").lower()
  if should_continue == "n": #find highest bid 
    continue_bidding = False
    find_highest_bidder(bids)
  elif should_continue == "y":
    print("\n"* 20 )#clear screen so no one sess previous bid
    #loop back

