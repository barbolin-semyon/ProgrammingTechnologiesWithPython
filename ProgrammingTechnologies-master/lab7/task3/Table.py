from lab7.Thing import Cultery
import string


class Table:
    __private_max_count_culteries = 3

    def __init__(self):
        self.__private_culteries = []

    def add_cultery(self, cultery: Cultery):
        if Table.__private_max_count_culteries == len(self.__private_culteries):
            return "Стол переполнен"
        else:
            self.__private_culteries.append(cultery)
            return str(cultery) + " - успешно положено на стол"

    def find_cultery_by_name(self, name: string):
        for i in self.__private_culteries:
            if i.get_name() == name:
                return i
        return None

    def find_cultery_by_price(self, price: int):
        for i in self.__private_culteries:
            if i.get_price() == price:
                return i

        return None

    def print_culteries_in_table(self):
        for i in self.__private_culteries:
            print(i)
