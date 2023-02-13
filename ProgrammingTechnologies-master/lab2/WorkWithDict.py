from PrintUtil import printTitleTask, printHeader

if __name__ == "__main__":
    printHeader("DICT")

    printTitleTask(6)
    task6()

    printTitleTask(8)
    task8()

    printTitleTask(12)
    task12()

    printTitleTask(14)
    task14()
def task6():
    my_dict = {1: 10, 'a': 5, 'b': -2}
    my_dict['a'] = 10
    print(my_dict)


def task8():
    my_dict = {1: 10, 'a': 5, 'b': -2, 15: 68, 2: -9, 6: 27}
    print(max(my_dict.values()))


def task12():
    my_dict = {1: 10, 'a': 5, 'b': -2, 15: 68, 2: -9, 6: 27}
    print(15 in my_dict.values())


def task14():
    my_dict = {'name': 'Alex', 'age':25, 'salary': 8000}
    keys = tuple(my_dict.keys())
    values = tuple(my_dict.values())
    print("keys:", keys)
    print("values:", values)