class House:
    def __init__(self, price):
        self._price = price

    @property   # define a property
    def price(self):    # use to access and modify outside the class
        return self._price

    @price.setter   # setter method for the price property
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("please enter a valid price")

    @price.deleter  # deleter method
    def price(self):
        del self._price

