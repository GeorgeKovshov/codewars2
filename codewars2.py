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
print(x("be free"))











