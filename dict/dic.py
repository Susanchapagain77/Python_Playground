import os 
num=int(input("How many bidders are there to bid for?\n"))
my_dict={}
def clear_console():
    """
    Clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
for i in range(num):
     
    name=input("Enter your name\n").lower()
    bid_price=float(input("enter your bid price\n$"))
    my_dict[name]=bid_price
    clear_console()
    
    
highest_bidder = max(my_dict, key=my_dict.get)
print(f"The highest bidder is {highest_bidder} with a bid price of ${my_dict[highest_bidder]:.2f}")
