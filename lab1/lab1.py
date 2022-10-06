import string

# ex1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


inp = list(map(int, input().split()))
print(inp)

res = inp[0]
for x in inp[1::]:
    res = gcd(x, res)

print(res)

# ex2

def check_vow(string, vowels):
    count = 0
    for character in string:
        if character in vowels:
            count += 1
    print(len(string), count)

check_vow('ana are mere', ['a', 'e', 'i', 'o', 'u'])

# ex3

string1 = 'ana'
string2 = 'ana ana ana mere ana'
print(string2.count(string1))

# ex4

def update_naming_conv(text):
    new_string = text[0].lower()
    for letter in text[1::]:
        if letter == ' ':
            continue
        elif 'A' <= letter <= 'Z':
            new_string = new_string + '_' + letter.lower()
        else:
            new_string = new_string + letter
    print(new_string)

update_naming_conv('ILoveSnakeCase')

# ex5

def print_matrix_spiral(mat):
    top = 0
    left = 0
    bottom = len(mat) - 1
    right = len(mat) - 1

    while True:
        if left > right:
            break

        # print top, from left to right
        for i in range(left, right+1):
            print(mat[top][i], end=' ')
        top += 1

        if top > bottom:
            break

        # print right, from top to bottom
        for i in range(top, bottom+1):
            print(mat[i][right], end=' ')
        right -= 1

        if left > right:
            break

        # print bottom, from right to left
        for i in range(right, left - 1, -1 ):
            print(mat[bottom][i], end=' ')
        bottom -= 1

        if top > bottom:
            break

        # print left, from bottom to right
        for i in range(bottom, top - 1, -1):
            print(mat[i][left], end=' ')
        left += 1

matrix = [['f', 'i', 'r', 's'],
          ['n', '_', 'l', 't'],
          ['o', 'b', 'a', '_'],
          ['h', 't', 'y', 'p']]

print(matrix)
print_matrix_spiral(matrix)

# ex6

number = 12321
if str(number) == str(number)[::-1]:
    print(number, 'is palindrome')
else:
    print(number, 'is not palindrome')

# ex7

text = 'abc123abc888'
number = ''
for index in range(0, len(text)):
    if '0' <= text[index] <= '9':
        for digit in range(index, len(text)):
            if '0' > text[digit] or text[digit] > '9':
                break
            number = number + text[digit]
        break

print(number)

# ex8

print(str(bin(55)).count('1'))

# ex9

dictionary = {}
text = 'an apple is not a tomato'.replace(' ', '')

for letter in text:
    if letter not in dictionary:
        dictionary[letter] = 1
    else:
        dictionary[letter] = dictionary[letter] + 1

max_letter = max(dictionary, key=dictionary.get)
print(max_letter, dictionary[max_letter])

# ex10

text = 'I love Python exam'
words = text.split()
print(len(words))