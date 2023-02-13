import string

import char as char

from PrintUtil import printHeader, printTitleTask


if __name__ == "__main__":
    printHeader("Decorate")

    printTitleTask(5)
    f = str_case_result(del_str)
    print(f("SkaTiK", 'a'))

    printTitleTask(7)
    f = celsius(temperature_fahrenheit)
    print(f(100))

    printTitleTask(8)
    f = check_type(reply_int)
    print(f(40))


def str_case_result(func):
    def decorator(line: string, symbol: char):
        result: string = func(line, symbol)
        avarage_index: int = len(result) // 2
        return result[: avarage_index].upper() + result[avarage_index] + result[avarage_index + 1:].lower()

    return decorator


def del_str(line: string, symbol: char):
    return line.replace(symbol, '')


def celsius(func):
    def decorator(temperature: float):
        result: float = func(temperature)
        return result / 33.8

    return decorator


def temperature_fahrenheit(temperature: float):
    return temperature


def check_type(func):
    def decorator(number):
        if isinstance(number, int):
            return func(number) * 2
        else:
            return None

    return decorator


def reply_int(number: int):
    return number
