import string
from Student import Student


class StudentGroup:
    def __init__(self, min_count: int, max_count: int):
        self.__min_count = min_count
        self.__max_count = max_count
        self.__students = []

    def add_student(self, student: Student) -> string:
        if len(self.__students) == self.__max_count: return "Группа переполнена"

        self.__students.append(student)
        return "Студент успешно добавлен"

    def remove_student(self, __name: string) -> string:
        index: int = self.__get_index_by_name_student(__name)
        if index != -1:
            self.__students.pop(index)
            return "Студент %s успешно отчислен" % __name
        return "Такого студента нет"

    def __get_index_by_name_student(self, name):
        for i in range(len(self.__students)):
            if name == self.__students[i].get_name():
                return i
        return -1

    def find_student(self, name: string) -> Student:
        for i in self.__students:
            if name == i.name:
                return i

    def print_students_(self):
        for student in self.__students:
            print(student)
