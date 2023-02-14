import string


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


if __name__ == "__main__":
    print("\nЗадание: 4")
    task4()

    print("\nЗадание: 5")
    task5()

    print("\nЗадание: 10")
    task10()
