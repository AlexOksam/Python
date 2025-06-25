# Auction Program
def find_highest_bidder(bidding_dict):
    winner = ""
    highest_bid = 0
    for bid in bidding_dict:
        if bidding_dict[bid] > highest_bid:
            highest_bid = bidding_dict[bid]
            winner = bid
    
    print(f"The winner is {winner} with a bid of {highest_bid} $")

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bidder(bids)
    else: should_continue == 'yes'
