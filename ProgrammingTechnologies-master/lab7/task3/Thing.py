import string

class Thing:
    def __init__(self, name: string, price: int):
        self.__private_name = name
        self.__private_price = price

    def get_name(self):
        return self.__private_name

    def get_price(self):
        return self.__private_price
    def __str__(self):
        return self.__private_name + "(" + str(self.__private_price) + "руб)"

class Cultery(Thing):
    def __init__(self, name: string, price: float):
        super().__init__(name, price)

