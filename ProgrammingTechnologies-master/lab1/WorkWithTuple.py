from PrintUtil import printHeader, printTitleTask


if __name__ == "__main__":
    printHeader("Tuple")

    printTitleTask(1)
    task1()

    printTitleTask(7)
    task7()

    printTitleTask(16)
    task16()

    printTitleTask(19)
    task19()

def task1():
    my_tuple = (1,2,5,6)
    print(len(my_tuple))

def task7():
    my_tuple = (0, -2, 81, 42, 6, 6, 23)
    print(max(my_tuple))

def task16():
    my_tuple = (1, 2, 3, 4, 5, 6, 2, 3, 2, 1, 2, 'a', 'b', 2, 5)
    print(my_tuple[-5:])

def task19():
    my_tuple = (0, -2, 5, 4, 6, 6, 1)
    print(sum(my_tuple))