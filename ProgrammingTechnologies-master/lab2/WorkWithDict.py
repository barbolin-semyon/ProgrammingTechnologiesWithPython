def task6():
    my_dict = {1: 10, 'a': 10, 'b': -2}
    print(my_dict)


def task8():
    my_dict = {1: 10, 'a': 5, 'b': -2, 15: 68, 2: -9, 6: 27}
    print(max(my_dict.values()))


def task12():
    my_dict = {1: 10, 'a': 5, 'b': -2, 15: 68, 2: -9, 6: 27}
    print(15 in my_dict.values())


def task14():
    my_dict = {'name': 'Alex', 'age': 25, 'salary': 8000}
    keys = tuple(my_dict.keys())
    values = tuple(my_dict.values())
    print("keys:", keys)
    print("values:", values)


if __name__ == "__main__":
    print("\nЗадание: 6")
    task6()

    print("\nЗадание: 8")
    task8()

    print("\nЗадание: 12")
    task12()

    print("\nЗадание: 14")
    task14()