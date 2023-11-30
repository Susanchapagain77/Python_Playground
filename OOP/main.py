class Item:
    def __init__(self,name: str,price: float,quantity=0):
        #run validation to the received arguments
        assert price>=0, f"Price{price} is not greater than 0"
        assert quantity>=0, f"Quantity{quantity} is not greater than 0"
        
        #assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity
        
        
        #function to calculate total price of Item
    def calculate_total_price(self):
        return self.price*self.quantity
        
        
item1=Item("phone",100,15)
item2=Item("laptop",500,7)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

