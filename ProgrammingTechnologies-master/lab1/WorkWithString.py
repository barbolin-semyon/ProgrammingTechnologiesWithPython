import string

from PrintUtil import printHeader, printTitleTask


if __name__ == "__main__":
    printHeader("STRINGS")

    printTitleTask(4)
    task4()

    printTitleTask(5)
    task5()

    printTitleTask(10)
    task10()

def task4():
    str1: string = "Цель работы: познакомиться с основными"
    str1 = str1.replace("о", "*")
    print(str1)


def task5():
    s1: string = input("Введите слово \n")
    s2: string = s1[0] + s1[len(s1) // 2] + s1[-1]
    print(s2)


def task10():
    s1: string = "Как дела?"
    print(s1[::-1])
