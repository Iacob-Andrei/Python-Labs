import re
import os

# Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of
# alphanumeric characters.
def ex1(inp):
    return re.findall(r"[a-zA-Z0-9]+", inp)


# Write a function that receives as a parameter a regex string, a text string and a whole number x, and returns those
# long-length x substrings that match the regular expression.
def ex2(regex, text, x):
    return list(filter(lambda a: len(a) == x, re.findall(regex, text)))


# Write a function that receives as a parameter a string of text characters and a list of regular expressions and
# returns a list of strings that match on at least one regular expression given as a parameter.
def ex3(text, regex):
    match_list = list()
    for reg in regex:
        for word in re.findall(reg, text):
            if word not in match_list:
                match_list.append(word)
    print(match_list)
    return match_list


# Write a function that receives as a parameter the path to a xml document and an attrs dictionary and returns those
# elements that have as attributes all the keys in the dictionary and values the corresponding values. For example,
# if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be those tags whose
# attributes are class="url" si name="url-form" si data-id="item".
def ex4(path, attrs):
    match_list = list()
    with open(path, "r") as file:
        xml_data = file.read()

        attributes = list()
        for key, value in attrs.items():
            attributes.append(f" {key}=\"{value}\"")

        search_string = r"(<(\w+)" + r"".join(attributes) + r">[^</\2>]*</\2>)"

        match_list += [x[0] for x in re.findall(search_string, xml_data)]
    print(match_list)
    return match_list


# Write another variant of the function from the previous exercise that returns those elements that have at least one
# attribute that corresponds to a key-value pair in the dictionary.
def ex5(path, attrs):
    match_list = list()
    with open(path, "r") as file:
        xml_data = file.read()

        attributes = list()
        for key, value in attrs.items():
            attributes.append(f" {key}=\"{value}\"")

        search_string = r"(<(\w+) [^>]*(" + r"|".join(attributes) + r")[^>]*>[^(<\2>)]*</\2>)"

        match_list += [x[0] for x in re.findall(search_string, xml_data)]
    print(match_list)
    return match_list


# Write a function that, for a text given as a parameter, censures words that begin and end with vowels. Censorship
# means replacing characters from odd positions with *.
def censor_text(input_text):
    input_text = input_text.group(0)
    censored = ''
    for index in range(len(input_text)):
        if index % 2 == 0:
            censored += input_text[index]
        else:
            censored += '*'
    return censored


def ex6(text):
    return re.sub(r"(a|e|i|o|u)\w+(a|e|i|o|u)", censor_text, text)


# Verify using a regular expression whether a string is a valid CNP.
def ex7(cnp):
    return None

if __name__ == '__main__':
    # print(ex1('Ana are 10 mere'))
    # print(ex2(r"\w+", "ana are 10 mere ananas", 3))
    # ex3("ana are 10 mere", [r"\d+", r"\w+"])
    # ex4("resources/ex5.xml", attrs={"class": "url", "name": "url-form", "data-id": "item"})
    # ex5("resources/ex5.xml", attrs={"class": "url", "name": "url-form", "data-id": "item"})
    # print(ex6("ana va fi enzurata"))
    ex7("5010909275565")
