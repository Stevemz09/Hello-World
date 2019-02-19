'''
Create a simple class
attributes - variables
methods - functions working usually with attributes
'''

class CashRegister:
    def __init__(self):
        # Attributes
        self.items = 0
        self.price = 0

    # Methods
    def update_register(self, price):
        self.items += 1
        self.price += price

    def display_register(self):
        return print('Number of items =', self.items, '\n Total price = ', self.price)

    def clean_register(self):
        self.items = 0
        self.price = 0

    def price_after_taxes(self):
        pass

    def discount(self):
        pass

register1 = CashRegister()
register1.update_register(2.25)
register1.update_register(0.55)
register1.update_register(99.99)
register1.display_register()

register2 = CashRegister()
register2.update_register(25000)
register2.display_register()
print(register2.items)
print('Clear register 1 and 2')
register1.clean_register()
register2.clean_register()
register1.display_register()
register2.display_register()
