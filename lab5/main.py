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
    return_list = []

    for element in inp:
        if type(element) in [int, float]:
            return_list.append(element)
    return return_list


# Write a function that receives a list with integers as parameter that contains an equal number of even and odd
# numbers that are in no specific order. The function should return a list of pairs (tuples of 2 elements) of numbers
# (Xi, Yi) such that Xi is the i-th even number in the list and Yi is the i-th odd number
def ex6(inp: list) -> list:
    odd = [x for x in inp if x % 2 == 0]
    even = [x for x in inp if x % 2 == 1]

    return list(zip(odd, even))


def generate_fibo(n: int) -> list:
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    first_n_fibo = [0, 1]
    for i in range(1, n - 1):
        first_n_fibo.append(first_n_fibo[i] + first_n_fibo[i - 1])
    return first_n_fibo


def sum_digits(x):
    return sum(map(int, str(x)))


# Write a function called process that receives a variable number of keyword arguments The function generates the
# first 1000 numbers of the Fibonacci sequence and then processes them in the following way: If the function receives
# a parameter called filters, this will be a list of predicates (function receiving an argument and returning
# True/False) and will retain from the generated numbers only those for which the predicates are True. If the
# function receives a parameter called limit, it will return only that amount of numbers from the sequence. If the
# function receives a parameter called offset, it will skip that number of entries from the beginning of the result
# list. The function will return the processed numbers.
def ex7(**kwargs):
    fibo = generate_fibo(1000)

    if "filters" in kwargs.keys():
        for f in kwargs["filters"]:
            fibo = list(filter(f, fibo))

    if "offset" in kwargs.keys():
        fibo = fibo[kwargs["offset"]:]

    if "limit" in kwargs.keys():
        fibo = fibo[:kwargs["limit"]]

    print(fibo)


# Write a function called print_arguments with one parameter named function. The function will return one new
# function which prints the arguments and the keyword arguments received and will return the output of the function
# receives as a parameter.
def add_numbers(a, b):
    return a + b


def multiply_by_two(x):
    return x * 2


def print_arguments(function):
    def f(*args, **kwargs):
        print(args, kwargs)
        return function(*args, **kwargs)
    return f


# Write a function called multiply_output with one parameter named function. The function will return one new
# function which returns the output of the function received multiplied by 2.

def multiply_by_three(x):
    return x * 3


def multiply_output(function):
    def f(*args, **kwargs):
        return 2 * function(*args, **kwargs)
    return f


# Write a function called augment_function with two parameters named function and decorators. decorators will be a
# list of functions which will have the same signature as the previous functions (print_arguments, multiply_output).
# augment_function will create a new function which is augmented using all the functions in the decorators list.
def augment_function(function, decorators):
    def f(*args, **kwargs):
        fun = function
        for decorator in decorators:
            fun = decorator(fun)
        return fun(*args, **kwargs)
    return f


# Write a function that receives a list of pairs of integers (tuples with 2 elements) as parameter (named pairs). The
# function should return a list of dictionaries for each pair (in the same order as in the input list) that contain
# the following keys (as strings): sum (the value should be sum of the 2 numbers), prod (the value should be product
# of the two numbers), pow (the value should be the first number raised to the power of the second number)
def ex9(pairs):
    return_list = list()
    for pair in pairs:
        return_list.append({"sum": (pair[0] + pair[1]),
                            "prod": (pair[0] * pair[1]),
                            "pow": (pair[0] ** pair[1])})
    return return_list


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

    # ex5([1111, "2", {"35": "a"}, {4, 5}, 5, 6, 3.0])

    # print(ex6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

    # ex7(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
    #     limit=2,
    #     offset=2)

    # 8a
    # augmented_multiply_by_two = print_arguments(multiply_by_two)
    # print(augmented_multiply_by_two(10))

    # augmented_add_numbers = print_arguments(add_numbers)
    # print(augmented_add_numbers(3, 4))

    # 8b
    # augmented_multiply_by_three = multiply_output(multiply_by_three)
    # print(augmented_multiply_by_three(10))

    # 8c
    decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
    x = decorated_function(3, 4)
    print(x)

    # print(ex9(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)]))
