import string


def str_case_result(func):
    def decorator(line: string, symbol):
        result: string = func(line, symbol)
        avarage_index: int = len(result) // 2
        return result[: avarage_index].upper() + result[avarage_index] + result[avarage_index + 1:].lower()

    return decorator


def del_str(line: string, symbol):
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
