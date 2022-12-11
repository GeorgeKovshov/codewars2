def disemvowel(string_):
    return "".join([y for y in [*string_] if y not in ["a", "e", "o", "i", "u", "A", "E", "U", "I", "O"]])


def disemvowel2(string):
    return "".join(c for c in string if c.lower() not in "aeiou")


print(disemvowel("This website is for losers LOL!"))


def open_or_senior(data):
    return ["Senior" if x[0] >= 55 and x[1] > 7 else "Open" for x in data if x[0] > 0 and x[1] in range(-2, 23)]


def openOrSenior2(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]


print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))

def basic_op(operator, value1, value2):
    return {
        '+': value1 + value2,
        '-': value1 - value2,
        '*': value1 * value2,
        '/': value1 / value2
    }[operator]

def basic_o2(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))

print(basic_op('*', 4, 7))


x = lambda word: 'I want to ' + word
#print(x("be free"))

def unique_in_order(iterabl):
    if type(iterabl) != list:
        iterable = [*iterabl]
    else:
        iterable = iterabl
    if iterable:
        lenght = len(iterable)
        i = 0
        result = []
        while i < lenght - 1:
            if iterable[i] != iterable[i + 1]:
                result.append(iterable[i])
            i+=1
        result.append(iterable[lenght-1])
        return result
    else:
        return []

#from itertools import groupby

#def unique_in_order(iterable):
#   return [k for (k, _) in groupby(iterable)]

def unique_in_order3(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

unique_in_order2 = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]


print(unique_in_order('AAAABBBCCDAABBB'))


def get_sum(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b+1))

def get_sum_mathematical(a, b):
    return (a + b) * (abs(a - b) + 1) // 2

#print(get_sum(4,1))

def row_sum_odd_numbers(n):
    i, number = 1, 1
    while i < n:
        j = 0
        while j < i:
            number += 2
            j += 1
        i += 1
    i = 0
    result = 0
    while i < n:
        print(number)
        result += number
        number += 2
        i += 1
    return result

def row_sum_odd_numbers2(n):
    return sum(range(n*(n-1)+1, n*(n+1), 2))

print(row_sum_odd_numbers(4))


def find_even_index(arr):
    result = [arr.index(x) for x in arr if sum(arr[:arr.index(x)]) == sum(arr[arr.index(x)+1:])]
    return result.pop() if result else -1
    #print(arr[:3])

def find_even_index2(arr):
    result = [ind for ind, x in enumerate(arr) if sum(arr[:ind]) == sum(arr[ind+1:])]
    return result[0] if result else -1

def find_even_index3(lst):
    left_sum = 0
    right_sum = sum(lst)
    for i, a in enumerate(lst):
        right_sum -= a
        if left_sum == right_sum:
            return i
        left_sum += a
    return -1


print(find_even_index2([20,10,30,10,10,15,35]))


import string
print("Alphabet from a-z:")
for letter in string.ascii_lowercase:
   print(letter, end =" ")
print("\nAlphabet from A-Z:")
for letter in string.ascii_uppercase:
   print(letter, end =" ")

def is_pangram(s):
    list = [*s.lower()]
    for x in string.ascii_lowercase:
        if x not in list:
            return False
    return True

def is_pangram2(s):
    return set(string.ascii_lowercase).issubset(s.lower())

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))

def greet(name):
    return "Hello, {} how are you doing today?".format(name)

print(greet('Shingles'))


list = string.ascii_lowercase
def next_letter(str):
    if str == "z":
        return "a"
    else:
        return list[list.index(str) + 1]

def last_survivor_iteration(string):
    i = 1
    result = ""
    length = len(string)
    while i < length + 1:
        j = 0
        alone = True
        while j < len(string) - i:
            if string[j] == string[-i]:
                alone = False
            j += 1
        if alone == True:
            result = string[-i] + result
        i += 1
    return result

def last_survivors_new(string):
    x = len(string)
    y = x + 1
    result = string
    while x < y:
        print(result)
        y = x
        result = last_survivor_iteration(result)
        x = len(result)
    return result


print(last_survivors_new("zzaaabsssaasszzs"))









