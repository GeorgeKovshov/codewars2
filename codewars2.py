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

print(get_sum(4,1))









