from PrintUtil import printTitleTask, printHeader


def mainWorkWithList():
    printHeader("LIST")

    printTitleTask(9)
    task9()

    printTitleTask(10)
    task10()

    printTitleTask(11)
    task11()

    printTitleTask(12)
    task12()

def task9():
    my_list = [1, -2, 43, -42, 59, 6, 23]
    print(6 in my_list)

def task10():
    my_list = ['a', 'b', 2, 5]
    my_list += [3, 't']
    print(*my_list)

def task11():
    my_list1 = ['a', 'b', 2, 5]
    my_list2 = [3, 't']
    my_list3 = my_list2 + my_list1
    print(*my_list3)

def task12():
    my_list = [1, 2, 3, 4, 5, 6, 2, 3, 2, 1, 2, 'a', 'b', 2, 5]
    my_list.reverse()
    print(*my_list)