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