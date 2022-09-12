import csv

class Item:
    pay_rate = 0.8 # pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #Run validations to the recieved arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than  or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to self object
        Item.all.append(self)

        # assigning attributes dynamically
    def calculate_total_price(self):
        return self.price * self.quantity
    #functions inside class are "methods."

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For example i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity} )"


print(Item.is_integer(6))

# item1 = Item("Phone", 100, 1)
# item1.apply_discount()
# print(item1.price)
# # item1.price = 100
# # item1.quantity = 5
# # print(item1.calculate_total_price(item1.price, item1.quantity))
#
# item2 = Item("Laptop", 1000, 3)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)
# # item2.price = 1000
# # item2.quantity = 3
# # print(item2.calculate_total_price(item2.price, item1.quantity))
#
# # print(type(item1))
# # print(type(item1.name))
# # print(type(item1.price))
# # print(type(item1.quantity))
#
# # random_str = "aaa"
# # print(random_str.upper())
#
# # print(item1.name)
# # print(item1.price)
# # print(item1.quantity)
# # print(item2.name)
# # print(item2.price)
# # print(item2.quantity)
#
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
#
# # NOTE: INSTANCE ATTRIBUTE
# # NOTE: CLASS ATTRIBUTE - AN ATTRIBUTE THAT IS GOING TO BELONG TO THE CLASS ITSELF
#
#
# # __dict__ show all attributes
# print(Item.__dict__) # All the attributes for the Class Level
# print(item1.__dict__) # All the attributes for the Instance Level
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)
