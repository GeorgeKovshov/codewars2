def bouncing_ball(h, bounce, window):
    if h <= 0 or window >= h or bounce >= 1 or bounce <= 0:
        return -1
    else:
        result = 1
        h = h * bounce
        while h > window:
            result += 2
            h = h * bounce
        return result


print(bouncing_ball(2, 0.5, 1))
print(bouncing_ball(3, 0.66, 1.5))

def add_binary(a,b):
    c = a + b
    result = ""
    while c:
        result = str(c % 2) + result
        c = c // 2
    return result

def add_binary2(a,b):
    return bin(a+b)[2:]

def add_binary3(a,b):
    return '{0:b}'.format(a + b)

print((add_binary(1,1)))

import math
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    """returns a list of numbers that are like this: 89^2 = 8^2 + 9^2 """
    result = []
    for number in range(a, b):
        digits_of_number = [*str(number)]
        sum_of_digits = 0
        for digit_index in range(0, len(str(number))):
            #first_number = int(y[0])
            sum_of_digits += pow(int(digits_of_number[digit_index]), digit_index + 1)
        if number == sum_of_digits:
            result.append(number)
    return result

def dig_pow(n):
    return sum(int(x)**y for y,x in enumerate(str(n), 1))

def sum_dig_pow2(a, b):
    return [x for x in range(a,b + 1) if x == dig_pow(x)]

def sum_dig_pow3(a, b):
    return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]


print(sum_dig_pow(1, 95))

def bar_triang(point_a, point_b, point_c):
    return[round((point_a[0] + point_b[0] + point_c[0])/3, 4), round((point_a[1] + point_b[1] + point_c[1])/3, 4)]


def bar_triang2(a, b, c):
    return [round(sum(x)/3.0, 4) for x in zip(a, b, c)]

print(bar_triang([4, 6], [12, 4], [10, 10]))

from collections import Counter

def find_waldo(crowd):
    # Return y (row) and x (column) coordinates of Waldo -> (0,0) is top-left
    waldo_count = Counter()
    for ind, x in enumerate(crowd):
        waldo_count += Counter(crowd[ind])
    waldo = waldo_count.most_common()[-1][0]
    print(waldo)
    waldo_location = [-1,-1]
    for ind, x in enumerate(crowd):
        if waldo in crowd[ind]:
            waldo_location = [ind, crowd[ind].index(waldo)]
    print(waldo_location)


from collections import defaultdict

def find_waldo2(crowd):
    d = defaultdict(list)
    for y, row in enumerate(crowd):
        for x, c in enumerate(row):
            if c.isalpha():  #if all are letters returns True
                d[c].append([y, x])
    return next(v[0] for k, v in d.items() if len(v) == 1)

def find_waldo3(crowd):
    flatmap = "".join(crowd)
    waldo = Counter(flatmap).most_common()[-1][0]
    return divmod(flatmap.find(waldo), len(crowd[0]))


print(find_waldo([
              "             ",           # Air
              "         w   ",           # Air with a bird
              "   w         ",           # Air with a bird
              "~~~~~~~~~~~~~",           # Sea
              ".~..~~.~~~..~",           # Waves on beach
              "...P......P..",           # Beach with some people
              "......P..P...",           # Beach with some people
              "..PW........."            # Beach with Waldo and presumably a friend next to him
            ]))
print(find_waldo([
              "                              ",           # Air
              "                              ",           # Air
              "            _                 ",           # Top of pyramid
              "          _____               ",           # Layer of pyramid
              "        _________             ",           # Layer of pyramid
              "  B  _______________   G   GG "
            ]))

def is_defended(attackers, defenders):
    victory = 0
    amount_of_fights = min(len(attackers), len(defenders))
    biggest_army = max(len(attackers), len(defenders))
    for ind in range(0, amount_of_fights):
        print(f"{attackers[ind]} vs {defenders[ind]}")
        if attackers[ind] > defenders[ind]:
            victory -= 1
            print("lost")
        elif attackers[ind] < defenders[ind]:
            victory += 1
            print("won")
        else:
            print("draw")
        print("victory", victory)
    if amount_of_fights != biggest_army:
        if len(attackers) == biggest_army:
            victory -= biggest_army - amount_of_fights
        else:
            victory += biggest_army - amount_of_fights
    return victory > 0 if victory != 0 else sum(attackers) <= sum(defenders)

def is_defended1(atks, defs):
    atkPow, defPow = sum(atks),sum(defs)
    survivors = len(defs) - len(atks) + sum((a>b)-(a<b) for a,b in zip(defs,atks))
    return survivors>0 if survivors else defPow>=atkPow

from itertools import zip_longest

def is_defended(attackers, defenders):
    s = t = 0
    for a, d in zip_longest(attackers, defenders, fillvalue = -1):
        s += (d > a) - (a > d)
        t += d - a
    return s > 0 or not s and t >= 0


#print(is_defended([1,3,5,7], [2,4,6,8]))
print(is_defended([10, 10, 1, 1], [4, 4, 7, 7]))

stri = "slgfjdsakg"
print(stri[::-1])

def other_angle(a, b):
    return int(180 - (a + b))

def solution(string):
    string
    return "".join([x for x in string[::-1]])

print(solution("hello"))


def mango(quantity, price):
    return (quantity - quantity//3)*price

def trim(phrase, size):
    """I'm just goofing about here"""
    return "".join([x if (ind<max(size, 3) and len(phrase)<=3) or (ind<size-3) else "" for ind, x in enumerate([*phrase]) if ind<=size-1]) + "..." if len(phrase)>size else phrase

def trim2(phrase, size):
    return phrase if size >= len(phrase) else phrase[:size if len(phrase) < 4 or size < 4 else (size-3)]+ "..."


phr="Creating kata is fun"

print(phr[:5])
print(trim("Creating kata is fun",7))
print(trim("Creating kata is fun",4))
print(trim("He",1))
print(trim("Hey", 2))

def are_you_playing_banjo(name):
    # Implement me!
    return f"{name} plays banjo" if name[0] in ['R', 'r'] else f"{name} does not play banjo"

print(are_you_playing_banjo("Rohn"))

def set_reducer(inp):
    if len(inp)==1:
        return inp[0]
    else:
        new_inp = []
        last_x = -1
        index = -1
        for x in inp:
            if x == last_x:
                new_inp[index] += 1
            else:
                index += 1
                new_inp.append(1)
                last_x = x
        return set_reducer(new_inp)


from itertools import groupby

def set_reducer2(arr):
    return arr[0] if len(arr)==1 else set_reducer([len([*g]) for k, g in groupby(arr)])


print(set_reducer([0, 4, 6, 8, 8, 8, 5, 5, 7]))












