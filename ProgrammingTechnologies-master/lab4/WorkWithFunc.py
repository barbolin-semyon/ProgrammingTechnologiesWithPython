import calendar
import datetime

def max_number(numbers: list):
    return max(numbers)


def add(list1: list, list2: list):
    return sum(list1) + sum(list2)

def find_list_index(numbers: list, element: int):
    for i in range(len(numbers)):
        if numbers[i] == element:
            return i
    return "None"

def month_days(numberMonth: int):
    if numberMonth < 1 or numberMonth > 12: return 0
    current_year = datetime.datetime.now().year
    return calendar.monthrange(current_year, numberMonth)[1]


def algebraic_sum(N: int, k: int = 2):
    sum = 0
    for i in range(1, N + 1): sum += i**k
    return sum

if __name__ == "__main__":
    print("\nЗадание: 1")
    print(max_number([1, 3, 21, 5]))

    print("\nЗадание: 3")
    print(add([1], [2, 3]))

    print("\nЗадание: 5")
    print(find_list_index([1, 3, 5, 7], 5))

    print("\nЗадание: 18")
    print(month_days(0))

    print("\nЗадание: 25")
    print(algebraic_sum(3))