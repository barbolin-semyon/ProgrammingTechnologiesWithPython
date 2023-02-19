import datetime
import string


class Student:
    def __init__(self, name: string, receipt_date: datetime):
        self.__name = name
        self.__receipt_date = receipt_date

    def __str__(self):
        return ("Фамилия: %s, Дата поступления: %s"
               % (self.__name, self.__receipt_date.strftime("%m/%d/%Y")))

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__receipt_date