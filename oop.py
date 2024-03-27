import csv

class Item:

    pay_rate = 0.8      # Pay rate after 20% discount
    all = []
    
    def __init__(self, name:str, price:float, quantity=0):
        
        # Run validate to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    # Calculate the total price
    def total_price(self):
        return self.price * self.quantity
    
    # Calculate the total price after discount
    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    # Instantiate file from CSV
    @classmethod
    def instatiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get("name"),
                price = float(item.get("price")),
                quantity = int(item.get("quantity")),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

#Item.instatiate_from_csv()
#print(Item.all)

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
