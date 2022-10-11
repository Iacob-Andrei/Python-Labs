from sympy import *


# Write a function to return a list of the first n numbers in the Fibonacci string.
def ex1(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    first_n_fibo = [1, 1]
    for i in range(1, n - 1):
        first_n_fibo.append(first_n_fibo[i] + first_n_fibo[i - 1])
    return first_n_fibo


# Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def ex2(list_of_numbers):
    prime_numbers = list()
    for number in list_of_numbers:
        if isprime(number):
            prime_numbers.append(number)
    return prime_numbers


# Write a function that receives as parameters two lists a and b and returns:
# (an intersected with b, a reunited with b, a - b, b - a)
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


# Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a
# start position (integer). The function will return the song composed by going through the musical notes beginning
# with the start position and following the moves given as parameter.
# Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]
def ex4(notes, moves, start_position):
    print(notes[start_position], sep=" ")
    for move in moves:
        print(notes[move], sep=" ")


# Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the
# elements under the main diagonal with 0 (zero).
def ex5(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < i:
                matrix[i][j] = 0
            print(matrix[i][j], end=" ")
        print()
    return matrix


# Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list
# containing the items that appear exactly x times in the incoming lists. Example: For the [1,2,3], [2,3,4],[4,5,6],
# [4,1, "test"] and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.
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


# Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element
# will be the greatest palindrome number.
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


# Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to
# True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the
# flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.
# Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e"
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


# Write a function that receives as parameter a matrix which represents the heights of the spectators in a stadium
# and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the
# game. A spectator can't see the game if there is at least one taller spectator standing in front of him. All the
# seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the
# closest row from the field. Example: # FIELD [[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7,
# 6, 7, 5]] Will return : [(2, 2), (3, 4), (2, 4)]
def ex9(matrix):
    spectators = list()
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            flag_can_see = True
            for spectator_in_front_poz in range(0, i):
                if matrix[i][j] <= matrix[spectator_in_front_poz][j]:
                    flag_can_see = False
                    break
            if not flag_can_see:
                spectators.append({i: j})
    print(spectators)


# Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple
# contains the first items in the lists, the second element contains the items on the position 2 in the lists,
# etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. Note: If
# input lists do not have the same number of items, missing items will be replaced with None to be able to generate
# max ([len(x) for x in input_lists]) tuples.
def ex10(*args):
    max_length = max(len(a) for a in args)
    new_list = list()
    for i in range(0, max_length):
        i_list = list()
        for arg_list in args:
            if i < len(arg_list):
                i_list.append(arg_list[i])
            else:
                i_list.append(None)
        new_list.append(i_list)
    print(new_list)


# Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
def sorting_rule(element):
    return element[1][2]


def ex11(list_of):
    list_of.sort(key=sorting_rule)
    print(list_of)


# Write a function that will receive a list of words  as parameter and will return a list of lists of words,
# grouped by rhyme. Two words rhyme if both of them end with the same 2 letters. Example: group_by_rhyme(['ana',
# 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]
def ex12(words):
    rhymes = list()
    for word in words:
        print(word[-2:])
        added = False
        for i in range(0, len(rhymes)):
            if rhymes[i][0][-2:] == word[-2:]:
                rhymes[i].append(word)
                added = True
                break
        if not added:
            rhymes.append([word])
    print(rhymes)


if __name__ == '__main__':
    # print(ex1(7))

    # print(ex2([1, 2, 4, 6, 7, 13, 11, 29, 83]))

    # ex3([1, 2, 3, 4, 5], [1, 2, 6, 8])

    ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)

    # ex5([[1, 1, 1, 1, 1, 1],
    #      [1, 1, 1, 1, 1, 1],
    #      [1, 1, 1, 1, 1, 1],
    #      [1, 1, 1, 1, 1, 1],
    #      [1, 1, 1, 1, 1, 1]])

    # ex6(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"])

    # ex7([111, 121, 909, 45, 12321])

    # ex8(["test", "hello", "lab002"], 2, False)

    # ex9([[1, 2, 3, 2, 1, 1],
    #      [2, 4, 4, 3, 7, 2],
    #      [5, 5, 2, 5, 6, 4],
    #      [6, 6, 7, 6, 7, 5]])

    # ex10([1,2,3], [5,6,7], ["a", "b", "c", "5"])

    # ex11([('abc', 'bcd'), ('abc', 'zza')])

    # ex12(['ana', 'banana', 'carte', 'arme', 'parte'])
