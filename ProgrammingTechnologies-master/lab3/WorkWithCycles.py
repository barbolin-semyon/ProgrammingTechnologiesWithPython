import math

from PrintUtil import printHeader, printTitleTask


if __name__ == "__main__":
    printHeader("Cycles")

    printTitleTask(1)
    task1()

    printTitleTask(3)
    task3()

    printTitleTask(8)
    task8()

    printTitleTask(10)
    task10()

    printTitleTask(20)
    task20()


def task1():
    my_list1 = [1, 2, 3, 4, 9, 7, 4, 5.3, 9.7, 3]
    sum: float = 0.0

    for i in my_list1: sum += i
    print(sum)


def task3():
    my_list1 = [1, 2, 3, 4, 9, 7, 4, 5.3, 9.7, 3]
    index: int = 0
    sum: float = 0.0

    while (index < len(my_list1)):
        sum += my_list1[index]
        index += 1

    print(sum)


def task8():
    my_list = [1, 2, 3, 4, 5, 6, 2, 3, 2, 1, 2]
    count: int = 0
    for i in my_list:
        if (i == 2): count += 1

    print(count)


def task10():
    count = 0
    for i in range(10, 76 + 1):
        if i % 3 == 0: count += 1

    print(count)

def task20():
    z: int = int(input("Введите число: "))
    result: float = 0

    for n in range(1, z + 1):
        numerator: float = math.sqrt(21 + math.sqrt(3**n))
        denominator: float = 3 / math.sin(n)
        result += numerator / denominator

    print(result)
