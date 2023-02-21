import string

printTitleTask(1)
    gen = my_generator(1, 100, 2)
    for i in gen: print(i, end = ' ')

    printTitleTask(3)
    gen = my_enumerate([9, 8, 7, 6, 5, 4, 3, 2, 1])
    for i in gen: print(i, end=' ')

    printTitleTask(7)
    gen = letters("Hello")
    for i in gen: print(i, end=' ')
def my_generator(start: int, end: int, step: int = 1):
    while start <= end:
        yield start
        start += step

def my_enumerate(list: int):
    index: int = 0
    for val in list:
        yield (index, val)
        index += 1

def letters(line: string):
    for i in line:
        yield i