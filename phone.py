from item import Item

class Phone(Item):
    # all = []
    def __init__(self, name:str, price:float, quantity=0, broken=0):
        
        #Call super function to have access to all attributes
        super().__init__(
            name, price, quantity
            )

        # Run validate to the received arguments
        # assert price >= 0, f"Price {price} is not greater than or equal to zero"
        # assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        assert broken >= 0, f"Quantity {broken} is not greater than or equal to zero"

        # Assign to self object
        # self.name = name
        # self.price = price
        # self.quantity = quantity
        self.broken = broken

        # Action to execute
        # Phone.all.append(self)

phone1 = Phone("iPhone", 1000, 100, 1)
phone2 = Phone("Samsung", 800, 25)
phone3 = Phone("Nokia", 500, 30)
phone4 = Phone("Motorola", 400, 20)
phone5 = Phone("LG", 300, 5)
phone6 = Phone("Vega", 200, 10)


# print(phone1.total_price())




#print("Total price for the items: ")
#print(f"{item1.name}: {item1.total_price()}")
#print(f"{item2.name}: {item2.total_price()}")
#print(f"{item3.name}: {item3.total_price()}")
#print(f"{item4.name}: {item4.total_price()}")
#print(f"{item5.name}: {item5.total_price()}")
#print(f"{item6.name}: {item6.total_price()}")
print(Item.all)
print(Phone.all)
    
#print(Item.is_integer(4.2))