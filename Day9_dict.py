
print("Welcome to the Auction Program")

dict = {}
continue_loop=True

while continue_loop:
    name=input("Type Your Name: ")
    bid=int(input("Type your bid: "))
    dict[name]=bid
    choice=input("Do you want to add more bids? (yes/no): ")
    if choice.lower() == "no":
        continue_loop = False
        print("\n"*80)
        print("Auction Ended")
        max_bidder = max(dict, key=dict.get)
        print(f"The highest bidder is {max_bidder} with a bid of ${dict[max_bidder]}")

   




    
    

