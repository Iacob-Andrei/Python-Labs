# Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a
# intersected with b, a reunited with b, a - b, b - a)
def ex1(a, b):
    a = set(a)
    b = set(b)

    return [a.intersection(b), a.union(b), a - b, b - a]


# Write a function that receives a string as a parameter and returns a dictionary in which the keys are the
# characters in the character string and the values are the number of occurrences of that character in the given text.
def ex2(inp):
    occurrences = dict()
    for chr in inp:
        if chr in occurrences:
            occurrences[chr] = 1 + occurrences[chr]
        else:
            occurrences[chr] = 1
    return occurrences


# Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must be
# recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
def ex3(dict_one, dict_two):
    for key in dict_one:
        if key not in dict_two:
            return False

    for key in dict_two:
        if key not in dict_one:
            return False

        if type(dict_two[key]) not in (dict, list):
            if dict_one[key] is not dict_two[key]:
                return False
        elif type(dict_one[key]) is not type(dict_two[key]):
            return False
        elif type(dict_two[key]) is dict:
            if not ex3(dict_one[key], dict_two[key]):
                return False
        elif type(dict_two[key]) is list:
            if dict_one[key] != dict_two[key]:
                return False

    return True


# The build_xml_element function receives the following parameters: tag, content, and key-value elements given as
# name-parameters. Build and return a string that represents the corresponding XML element. Example:
# build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns
# the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"
def ex4(tag, content, **kwargs):
    out = "<" + tag
    for arg in kwargs:
        out = out + " " + arg + "=\"" + kwargs[arg] + "\""
    out = out + "> " + content + " </" + tag + ">"
    return out


# The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a
# dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: (key, "prefix",
# "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value (not at
# the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all the
# rules, False otherwise.
def find_rule(rules, value):
    for rule in rules:
        if rule[0] is value:
            return rule
    return False


def validate_rule(rule, text):
    return text.startswith(rule[1]) and text.endswith(rule[3]) and text.__contains__(rule[2])


def ex5(rules: [any], dictionary: {any}):
    for key in dictionary.keys():
        rule = find_rule(rules, key)
        if rule is False:
            print(key, dictionary[key], "|| has no key")
            return False
        else:
            if not validate_rule(rule, dictionary[key]):
                return False
    return True


# Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique
# elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve this
# objective).
def ex6(inp):
    a = b = 0
    for element in set(inp):
        if inp.count(element) == 1:
            a += 1
        else:
            b += 1
    return a, b


# Write a function that receives a variable number of sets and returns a dictionary with the following operations
# from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b",
# where a and b are two sets, and op is the applied operator: |, &, -.
def operations(a, b):
    out = dict()
    out.update({str(a) + " | " + str(b): a.union(b)})
    out.update({str(a) + " & " + str(b): a.intersection(b)})
    out.update({str(a) + " - " + str(b): a - b})
    out.update({str(b) + " - " + str(a): b - a})
    return out


def ex7(*args):
    out = dict()
    for i in range(0, len(args)):
        a = args[i]
        for j in range(i + 1, len(args)):
            b = args[j]
            out.update(operations(a, b))
    print(out)


# Write a function that receives a single dict parameter named mapping. This dictionary always contains a string key
# "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping in the
# following way: the value of the current key is the key for the next value, until you find a loop (a key that was
# visited before). The function must return the list of objects obtained as previously described
def ex8(mapping):
    element = mapping['start']
    out = [element]
    while True:
        element = mapping[element]
        if element in out:
            break
        else:
            out.append(element)
    return out


# Write a function that receives a variable number of positional arguments and a variable number of keyword arguments
# and will return the number of positional arguments whose values can be found among keyword arguments values. Ex:
# my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return 3
def ex9(*args, **kwargs):
    count = 0
    for arg in args:
        if arg in kwargs.values():
            count += 1
    return count


if __name__ == '__main__':
    # print(ex2("Ana has apples"))
    print(ex3({2: {2: 3}, 44: [3, 2]}, {2: {2: 3}, 44: [3, 2]}))
    # print(ex4("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))
    # print(ex5({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
    #           {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))
    # print(ex6([1, 1, 1, 2, 3, 3]))
    # ex7({1, 2}, {2, 3})
    # print(ex8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
    # print(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
