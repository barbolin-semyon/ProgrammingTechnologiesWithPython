def task3():
    inputValue: int = 2
    inputValue = inputValue << 4
    print(bin(inputValue))


def task5():
    z: int = 0b1011010
    print(z % 10 == 1)


def task8():
    z: int = 149
    count = 0
    while (z != 0):
        count += z & 1
        z = z >> 1
    print(count)


def task10():
    z: int = 512
    z = z >> 2
    print(z)


if __name__ == "__main__":
    print("\nЗадание: 3")
    task3()

    print("\nЗадание: 5")
    task5()

    print("\nЗадание: 8")
    task8()

    print("\nЗадание: 10")
    task10()
