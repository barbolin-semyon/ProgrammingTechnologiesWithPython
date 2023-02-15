import math

def task2():
    val1: int = 10
    val2: int = int(input("Введите число"))
    print(val1 * val2)
def task3():
    val1: int = int(input("Введите основание"))
    val2: int = int(input("Введите степень"))

    print(val1 ** val2)

def task6():
    val1: int = 157
    print(157 % 3)
def task12():
    n: int = int(input("Введите число"))
    result: float = (n - 20) / math.sqrt(n**3)
    print(result)
def task18():
    n: int = int(input("Введите число"))

    numerator: float = math.sqrt(21 + math.sqrt(3**n))
    denominator: float = 3 / math.sin(n)
    result: float = numerator / denominator

    print(result)

if __name__ == "__main__":
    print("\nЗадание: 2")
    task2()

    print("\nЗадание: 3")
    task3()

    print("\nЗадание: 6")
    task6()

    print("\nЗадание: 12")
    task12()

    print("\nЗадание: 18")
    task18()