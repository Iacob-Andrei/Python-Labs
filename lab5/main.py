import utils


# Create a function and an anonymous function that receive a variable number of arguments. Both will return the sum
# of the values of the keyword arguments.
def suma(*args, **kwargs):
    print(sum(kwargs.values()))


def ex2():
    suma(1, 2, c=3, k=4)
    anonymous = lambda *args, **kwargs: print(sum(kwargs.values()))
    anonymous(1, 2, c=3, k=4)


# Using functions, anonymous functions, list comprehensions and filter, implement three methods to generate a list
# with all the vowels in a given string.
def check_with_function(input_text: str) -> list[str]:
    return [x for x in input_text if x in 'aeiou']


def check_with_filter(input_text: str) -> list[str]:
    return list(filter(lambda x: x in "aeiou", input_text))


def ex3():
    print(f'With function: {check_with_function("Programming in Python is fun")}')

    with_lambda = lambda inp_text: [x for x in inp_text if x in 'aeiou']
    print(f'With lambda: {with_lambda("Programming in Python is fun")}')

    print(f'With filter: {check_with_filter("Programming in Python is fun")}')


# Write a function that receives a variable number of arguments and keyword arguments. The function returns a list
# containing only the arguments which are dictionaries, containing minimum 2 keys and at least one string key with
# minimum 3 characters.
def ex4(*args, **kwargs) -> list:
    return_list = list()
    for arg in args:
        if type(arg) is dict and len(arg) >= 2:

            for key in arg.keys():
                if type(key) == str and len(key) >= 3:
                    return_list.append(arg)
                    break

    for arg in kwargs.values():
        if type(arg) is dict and len(arg) >= 2:

            for key in arg.keys():
                if type(key) == str and len(key) >= 3:
                    return_list.append(arg)
                    break

    print(return_list)
    return return_list


# Write a function with one parameter which represents a list. The function will return a new list containing all the
# numbers found in the given list.
def ex5(inp: list) -> list:
    print(str(inp))

    return []


# Write a function that receives a list with integers as parameter that contains an equal number of even and odd
# numbers that are in no specific order. The function should return a list of pairs (tuples of 2 elements) of numbers
# (Xi, Yi) such that Xi is the i-th even number in the list and Yi is the i-th odd number
def ex6(inp: list) -> list:
    odd = [x for x in inp if x % 2 == 0]
    even = [x for x in inp if x % 2 == 1]

    return list(zip(odd, even))


if __name__ == '__main__':
    # ex2()
    # ex3()

    # ex4({1: 2, 3: 4, 5: 6},
    #     {'a': 5, 'b': 7, 'c': 'e'},
    #     {2: 3},
    #     [1, 2, 3],
    #     {'abc': 4, 'def': 5},
    #     3764,
    #     dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
    #     test={1: 1, 'test': True})

    # ex5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0])

    print(ex6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

