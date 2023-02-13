import string

from PrintUtil import printHeader, printTitleTask


if __name__ == "__main__":
    printHeader("RECURSION")

    printTitleTask(4)
    print(closure_sum(1)(2))

    printTitleTask(5)
    print(closure_comparison('>')('>'))

    printTitleTask(10)
    print(closure_list_del([1, 3, 12, 14, 15, 17])(3))


def closure_sum(number: int):
    def inner(inner_number: int):
        return inner_number + number

    return inner


def closure_comparison(symbol: string):
    true_symbols = ['>', '<', '=']

    def inner(inner_symbol: string):
        return inner_symbol == symbol and symbol in true_symbols

    return inner


def closure_list_del(numbers: list):
    def inner(n: int):
        return [i for i in numbers if i % n != 0]

    return inner
