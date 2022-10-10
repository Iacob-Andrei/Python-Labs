from sympy import *


def ex1(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [2]

    first_n_fibo = [1, 1]
    for i in range(1, n - 1):
        first_n_fibo.append(first_n_fibo[i] + first_n_fibo[i - 1])
    return first_n_fibo


def ex2(list_of_numbers):
    prime_numbers = list()
    for number in list_of_numbers:
        if isprime(number):
            prime_numbers.append(number)
    return prime_numbers


def ex3(a, b):
    a = set(a)
    b = set(b)
    c = list()
    print(f"A intersect B {a.intersection(b)}")
    c.append(a.intersection(b))
    print(f"A union B {a.union(b)}")
    c.append(a.union(b))
    print(f"A - B {a - b}")
    c.append(a - b)
    print(f"B - A {b - a}")
    c.append(b - a)


def ex4(notes, moves, start_position):
    print(notes[start_position], sep=" ")
    for move in moves:
        print(notes[move], sep=" ")


def ex5(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < i:
                matrix[i][j] = 0
            print(matrix[i][j], end=" ")
        print()
    return matrix


def ex6(x, *args):
    count_app = dict()
    for a in args:
        if len(a) > 1:
            for item in a:
                if item not in count_app:
                    count_app[item] = 1
                else:
                    count_app[item] = count_app[item] + 1

    items_with_occurrences_x = list()
    for item in count_app.keys():
        if count_app[item] == x:
            items_with_occurrences_x.append(item)
    print(items_with_occurrences_x)
    return items_with_occurrences_x


def ex7(values):
    number_of_palindrome = 0
    greatest_palindrome = -1

    for value in values:
        if str(value) == str(value)[::-1]:
            number_of_palindrome += 1
            if value > greatest_palindrome:
                greatest_palindrome = value

    print(number_of_palindrome, greatest_palindrome)
    return number_of_palindrome, greatest_palindrome


def ex8(strings, x=1, flag=True):
    returning_list = list()
    for text in strings:
        word_character = list()
        for character in text:
            is_divisible = ord(character) % x
            if is_divisible == 0 and flag:
                word_character.append(character)
            elif is_divisible == 1 and not flag:
                word_character.append(character)
        returning_list.append(word_character)
    print(returning_list)


if __name__ == '__main__':
    # print(ex1(7))
    # print(ex2([1, 2, 4, 6, 7, 13, 11, 29, 83]))
    # ex3([1, 2, 3, 4, 5], [1, 2, 6, 8])
    # ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
    # ex5([[1, 1, 1, 1, 1, 1],
    #      [1, 1, 1, 1, 1, 1],
    #      [1, 1, 1, 1, 1, 1],
    #      [1, 1, 1, 1, 1, 1],
    #      [1, 1, 1, 1, 1, 1]])
    # ex6(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"])
    # ex7([111, 121, 909, 45, 12321])
    # ex8(["test", "hello", "lab002"], 2, False)

