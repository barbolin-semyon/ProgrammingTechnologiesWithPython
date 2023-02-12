from PrintUtil import printTitleTask, printHeader

def mainWorkWithBitOperations():
    printHeader("BIT OPERATIONS")

    printTitleTask(3)
    task3()

    printTitleTask(5)
    task5()

    printTitleTask(8)
    task8()

    printTitleTask(10)
    task10()
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
    z= z >> 2
    print(z)