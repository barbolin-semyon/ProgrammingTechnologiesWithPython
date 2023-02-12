import string

from PrintUtil import printHeader, printTitleTask


def mainWorkWithControlConstuctors():
    printHeader("CONTROL CONSTRUCTORS")

    printTitleTask(1)
    task1()

    printTitleTask(5)
    task5()

    printTitleTask(7)
    task7()

    printTitleTask(15)
    task15()

    printTitleTask(18)
    task18()


def task1():
    month: int = int(input("Введите месяц(числом): "))
    if 0 < month < 13:
        month %= 12
        if month < 3:
            print("Зима")
        elif (month < 6):
            print("Весна")
        elif (month < 9):
            print("Лето")
        else:
            print("Осень")
    else:
        print("Ошибка ввода!")


def task5():
    val1: int = int(input("Введите оклад: "))

    if (val1 > 100000):
        val1 -= val1 / 100 * 13
    else:
        val1 -= val1 / 100 * 6

    print(val1)

def task7():
    my_list = [int(i) for i in input().split()]
    if (my_list[len(my_list) / 2] >= 10):
        print(my_list[0] + my_list[-1])
    else:
        print(my_list[0] * my_list[-1])


def task15():
    age: int = int(input("Введите свой возраст: "))
    if (age >= 18): print("YES")
    else: print("NO")

def task18():
    input_text: string = input("Введите курс: ")
    course: float = float(input_text.split("R")[1]) / int(input_text[1])
    request: string = input("Введите запрос: ")

    if request[-1] == "$":
        print(course * float(request[:-1]), "R", sep="")
    else:
        print(float(request[:-1]) / course, "$", sep="")
