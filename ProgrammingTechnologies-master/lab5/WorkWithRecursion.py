import string

def recursion_max(numbers: list) -> int:
    if len(numbers) == 1: return numbers[0]

    if numbers[0] <= numbers[1]:
        numbers.pop(0)
    else:
        numbers.pop(1)

    return recursion_max(numbers)


def factorial(n: int) -> int:
    if (n == 1): return 1
    return n * factorial(n - 1)


def remove_v(text: string) -> string:
    if len(text) == 0: return ''

    symbol: string = ''
    if text[0] != 'v': symbol += text[0]

    return symbol + remove_v(text[1:])


def recursion_gcd(number1: int, number2: int) -> int:
    if number1 == number2: return number1

    if number1 > number2:
        return recursion_gcd(number1 - number2, number2)
    else:
        return recursion_gcd(number2 - number1, number1)

if __name__ == "__main__":
    print("\nЗадание: 3")
    print(recursion_max([1, 11, 66, 10]))

    print("\nЗадание: 5")
    print(factorial(4))

    print("\nЗадание: 8")
    print(remove_v("rvvvvrrv"))

    print("\nЗадание: 10")
    print(recursion_gcd(36, 13))