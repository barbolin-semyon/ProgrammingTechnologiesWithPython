
if __name__ == "__main__":
    print("\nЗадание: 8")
    task8()

    print("\nЗадание: 10")
    task10()

    print("\nЗадание: 11")
    task11()

    print("\nЗадание: 12")
    task12()

def task8():
    my_list = [1, 0, 'Hi', 10]
    my_set = {3, 5, 'b'}
    my_set.update(my_list)
    print(*my_set)

def task10():
    my_str = 'Найдите сумму его неповторяющихся элементов'
    my_set = set(my_str)
    print(*my_set)

def task11():
    list1 = [1, 0, 1, 10, 5, 6, 7, 4, 4, 1, 6, 2, 5]
    temp_set = set(list1)
    print(list(temp_set))

def task12():
    A = {0, 1, 2, 6, 7, 8, 9}
    B = {1, 3, 6, 10, 21, 5}
    print(A.intersection(B))

