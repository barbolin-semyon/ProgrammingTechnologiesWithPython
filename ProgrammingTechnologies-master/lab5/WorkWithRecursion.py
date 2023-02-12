import string

from PrintUtil import printHeader, printTitleTask


def mainWorkWithRecursion():
    printHeader("RECURSION")

    printTitleTask(3)
    print(recursion_max([1, 11, 66, 10]))

    printTitleTask(5)
    print(factorial(4))

    printTitleTask(8)
    print(remove_v("rvvvvrrv"))

    printTitleTask(10)
    print(recursion_gcd(36, 13))


def recursion_max(numbers: list):
    if len(numbers) == 1: return numbers[0]

    if numbers[0] <= numbers[1]:
        numbers.pop(0)
    else:
        numbers.pop(1)

    return recursion_max(numbers)


def factorial(n: int):
    if (n == 1): return 1
    return n * factorial(n - 1)


def remove_v(text: string):
    if len(text) == 0: return ''

    symbol: string = ''
    if text[0] != 'v': symbol += text[0]

    return symbol + remove_v(text[1:])


def recursion_gcd(number1: int, number2: int):
    if number1 == number2: return number1

    if (number1 > number2):
        return recursion_gcd(number1 - number2, number2)
    else:
        return recursion_gcd(number2 - number1, number1)