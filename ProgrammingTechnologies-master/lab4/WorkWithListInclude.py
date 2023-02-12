from PrintUtil import printTitleTask, printHeader


def mainWorkWithListInclusion():
    printHeader("LISTINCLUSIONS")

    printTitleTask(4)
    task4()

    printTitleTask(5)
    task5()

    printTitleTask(10)
    task10()


def task4():
    my_list = [i for i in range(-43, 57 + 1, 14)]
    print(*my_list)


def task5():
    N: int = int(input("Введите размер матрицы: "))
    matrix = [[1 for i in range(N)] for i in range(N)]
    for line in matrix: print(line)

def task10():
    my_list = [i for i in range(1, 100 + 1) if '1' in ("%d" % i)]
    print(*my_list)