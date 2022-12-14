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



def last_survivors1(string):
    list1 = [*string]
    print(list1)
    new_letter = ""
    pre_letter = ""
    result = []
    for letter1 in list1:
        if letter1 == pre_letter:
            result.pop()
            result.append(next_letter(letter1))
            new_letter = next_letter(letter1)
        elif letter1 == new_letter:
            result.pop()
            result.append(letter1)
        else:
            result.append(letter1)
        pre_letter = letter1
    result1 = "".join([x for x in result])
    if result1 == string:
        return result1
    else:
        return last_survivors(result1)

def test(string):
    list1 = [*string]
    letter1 = "a"
    result = "{}".format(next_letter(letter1))
    for x in list1:
        result += x
        print(result)
    return result

def last_survivors(string):
    list1 = [*string]
    result = ""
    for ind1, letter1 in enumerate(list1):
        for ind2, letter2 in enumerate(list1):
            if letter1 == letter2 and ind1 != ind2:
                del list1[ind2]
                list1.remove(letter1)
                result = "{}".format(next_letter(letter1))
                for x in list1:
                    result += x
                print(result)
                return last_survivors(result)
    return "".join(list1)


def last_survivors3(string):
    ans = list(string);
    abc = list(map(chr, range(97, 123)))  # all letters
    abc.append('a')  # append the first letter at last z - a - b ...

    for f in range(len(string)):
        for i in ans:
            if ans.count(i) >= 2:
                index = abc.index(i)
                ans.remove(i);
                ans.remove(i)
                ans.append(abc[index + 1])

    return "".join(ans)

from collections import Counter

def shift(c):
    return chr( (ord(c) - 96) % 26 + 97 )

def last_survivors4(string):
    c = Counter(string)
    while True:
        for k,v in c.items():
            if v > 1:
                c[k] = v % 2
                c[shift(k)] += v // 2
                break
        else:
            return "".join(c.elements())

def last_survivors5(s):
    new = "abcdefghijklmnopqrstuvwxyza"
    for i in s:
        if s.count(i)>1:
            s = s.replace(i,"",2)+new[new.index(i)+1]
            return last_survivors(s)
    return s


#print(test("abcde"))
print(last_survivors("zzaaabsssaasszzs"))









