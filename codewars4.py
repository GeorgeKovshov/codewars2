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


def reduce_fraction(fraction):
    i = min(abs(fraction[0]), abs(fraction[1]))
    new_fraction = fraction
    print(fraction)
    while i>1:
        if fraction[0] % i == 0 and fraction[1] % i == 0:
            return reduce_fraction([fraction[0] / i, fraction[1] / i])
            break
        i -= 1
    return fraction

from fractions import Fraction
def reduce_fraction2(fraction):
    t = Fraction(*fraction)
    return (t.numerator, t.denominator)



def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def reduce_fraction3(fraction):
    num, denom = fraction
    gcd_num_denom = gcd(num, denom)
    return (num // gcd_num_denom, denom // gcd_num_denom)

print(reduce_fraction([60, 20]))

def descending_order(num):
    list = sorted([int(x) for x in str(num)], reverse=True)
    result = 0
    for x in list:
        result = result * 10 + x
    return result

def Descending_Order2(num):
    return int("".join(sorted(str(num), reverse=True)))


print(descending_order(123456789))

def reverse_words(text):
    """
    text_new = text.split(" ")
    text_n = ""
    for x in text.split(" "):
        text_n += " " + "".join(reversed(x))
    return text_n[1:]
    """
    return " ".join(["".join(reversed(x)) for x in text.split(" ")])[1:]

print(reverse_words('The quick brown fox jumps over the lazy dog.'))

domains_list = '''\
*.amazon.co.uk    89
*.doubleclick.net    139
*.fbcdn.net    212
*.in-addr.arpa    384
*.l.google.com    317
1.client-channel.google.com    110
6.client-channel.google.com    45
a.root-servers.net    1059
apis.google.com    43
clients4.google.com    71
clients6.google.com    81
connect.facebook.net    68
edge-mqtt.facebook.com    56
graph.facebook.com    150
mail.google.com    128
mqtt-mini.facebook.com    47
ssl.google-analytics.com    398
star-mini.c10r.facebook.com    46
staticxx.facebook.com    48
www.facebook.com    178
www.google.com    162
www.google-analytics.com    127
www.googleapis.com    87'''


def count_domains(domains, min_hits=0):
    dom = domains.split()
    i = 0
    dict = {}
    indexes = []
    while i < len(dom) - 1:
        sentence = dom[i].split(".")
        #if len(sentence[-2]) < 4 and len(sentence[-1]) == 2:  # in case of something like amazon.co.uk
        if sentence[-2] in ["co", "com"]:
            try:
                site = str(sentence[-3]) + "." + str(sentence[-2]) + "." + str(sentence[-1])
            except:
                site = str(sentence[-2]) + "." + str(sentence[-1])
        else:
            site = str(sentence[-2]) + "." + (sentence[-1])
        try:
            dict[site] += int(dom[i + 1])
        except:
            dict[site] = int(dom[i + 1])
        i += 2
        if dict[site] > min_hits and site not in indexes:
            indexes.append(site)
    new_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: (-item[1], item[0]))}
    result = ""

    for x in new_dict:
        if x in indexes:
            result = result + x + " (" + str(new_dict[x]) + ")" + "\n"
    return result[0:len(result) - 1]


print(count_domains(domains_list, 500))


"""
'livejasmin.com (1164)\n \ livejasmin.com (1164)\n '
'globo.com (925)\n' \ 'globo.com (925)\n
'booking.com (734)\n' \ "booking.com (734)\n"
'microsoftonline.com (633)\n' \ "microsoftonline.com (633)\n"
'fc2.com (613)\n' \ "fc2.com (613)\n"
'rakuten.co.jp (576)\n' \ "rakuten.co.jp (576)\n"
'diply.com (557)\n' \ "diply.com (557)\n"
'twitch.tv (484)\n' \ "twitch.tv (484)\n"
'cnzz.com (482)\n' \"cnzz.com (482)\n"
'linkedin.com (482)\n' \"linkedin.com (482)\n"
'baidu.com (479)\n' \"adobe.com (479)\n"
'adobe.com (479)\n' \"baidu.com (479)\n"
'naver.com (475)\n' \"naver.com (475)\n"
'tmall.com (473)\n' \"tmall.com (473)\n"
'walmart.com (471)\n' \"walmart.com (471)\n"
'txxx.com (469)\n' \"txxx.com (469)\n"
'labh.360.cn (463)' "360.cn (463)"
"""

def nb_dig(n, d):
    count = 0
    while n > 0:
        k = n*n
        print([*str(k)])
        for digit in [*str(k)]:
            if str(d) == digit:
                count += 1
        n -= 1
    return count

print(nb_dig(10,1))

print([*"123456"])


rod1 = []
rod2 = []
rod3 = []
def func(targeted_rod):
    """the most frequent action is the movement of the top 2 disks (the last rod):

                  [..2,1] [..]   [..]
        1 count:  [..2]   [..1]  [..]
        2 count:  [..]    [..1]  [..2]
        3 count:  [..]    [..]   [..2,1]

    so I've put it into a separate function.
    """
    global rod1
    global rod2
    global rod3

    # determening where the top 2 disks are and removing them
    if 1 in rod1:
        rod1.pop()
        rod1.pop()
    elif 1 in rod2:
        rod2.pop()
        rod2.pop()
    else:
        rod3.pop()
        rod3.pop()

    # putting the top 2 disks onto targeted rod
    if targeted_rod == 1:
        rod1.append(2)
        rod1.append(1)
    elif targeted_rod == 2:
        rod2.append(2)
        rod2.append(1)
    elif targeted_rod == 3:
        rod3.append(2)
        rod3.append(1)

def func1(targeted_rod):
    """the most frequent action is the movement of the top 2 disks (the last rod):

                  [..2,1] [..]   [..]
        1 count:  [..2]   [..1]  [..]
        2 count:  [..]    [..1]  [..2]
        3 count:  [..]    [..]   [..2,1]

    so I've put it into a separate function.
    """
    global rod1
    global rod2
    global rod3

    # putting the top 2 disks onto targeted rod
    if targeted_rod == 1:
        rod1.append(2)
        rod1.append(1)
    elif targeted_rod == 2:
        rod2.append(2)
        rod2.append(1)
    elif targeted_rod == 3:
        rod3.append(2)
        rod3.append(1)


def old_hanoi(disks):
    "function that returns the count of moves to win a hanoi tower game with the given number of disks"
    global rod1
    global rod2
    global rod3

    # if 1 or 2 disks, return count 1 or 2
    if disks < 3:
        return disks

    # putting the disks onto the first rod
    while disks >0:
        rod1.append(disks)
        disks -= 1

    # making the first 3 moves that place 1st and 2nd disks onto second rod
    func(2)
    count = 3

    # we have to keep track of where the last and current disk are moved from and to
    previous = 0
    current = 0
    future = 0
    while rod1 or (rod2 and rod3):  # if two rods are empty at the same time, then we have won the game and stop
        previous = current

        """
        in the cycle we compare the two rods that DON'T have the top two disks (1 and 2)
        and move from the rod with the smallest top disk to the one with the larger one.
        
        for visual clarity I used the nested ifs
        """

        if rod1 and rod1[-1] == 1:  # the exchange is between rod2 and rod 3
            if rod2 and (not rod3 or rod2[-1] < rod3[-1]):
                rod3.append(rod2.pop())
                current = 2
                future = 3
            else:
                rod2.append(rod3.pop())
                current = 3
                future = 2

        elif rod2 and rod2[-1] == 1:    # the exchange is between rod1 and rod 3
            if rod3 and (not rod1 or rod3[-1] < rod1[-1]):
                rod1.append(rod3.pop())
                current = 3
                future = 1
            else:
                rod3.append(rod1.pop())
                current = 1
                future = 3

        elif rod3 and rod3[-1] == 1:    # the exchange is between rod1 and rod 2
            if rod2 and (not rod1 or rod2[-1] < rod1[-1]):
                rod1.append(rod2.pop())
                current = 2
                future = 1
            else:
                rod2.append(rod1.pop())
                current = 1
                future = 2

        """ 
        if two disks are moved from the same rod (current and previous) one after the other
        then we move the top 2 disks to the rod they came from (current),
        else we move the top 2 disks to the rod that the last disk is moved to (future)
        """
        if previous == current:
            func(current)
        else:
            func(future)
        count += 3 + 1

    return count



rod1 = []
rod2 = []
rod3 = []
def func(targeted_rod):
    """the most frequent action is the movement of the top 2 disks (the last rod):

                  [..2,1] [..]   [..]
        1 count:  [..2]   [..1]  [..]
        2 count:  [..]    [..1]  [..2]
        3 count:  [..]    [..]   [..2,1]

    so I've put it into a separate function.
    """
    global rod1
    global rod2
    global rod3

    # determening where the top 2 disks are and removing them
    if 1 in rod1:
        rod1.pop()
        rod1.pop()
    elif 1 in rod2:
        rod2.pop()
        rod2.pop()
    else:
        rod3.pop()
        rod3.pop()

    # putting the top 2 disks onto targeted rod
    if targeted_rod == 1:
        rod1.append(2)
        rod1.append(1)
    elif targeted_rod == 2:
        rod2.append(2)
        rod2.append(1)
    elif targeted_rod == 3:
        rod3.append(2)
        rod3.append(1)

def good_hanoi(disks):
    "function that returns the count of moves to win a hanoi tower game with the given number of disks"
    global rod1
    global rod2
    global rod3

    # if 1 or 2 disks, return count 1 or 2
    if disks < 3:
        return disks

    # putting the disks onto the first rod
    while disks >0:
        rod1.append(disks)
        disks -= 1

    # making the first 3 moves that place 1st and 2nd disks onto second rod
    #func(2)
    rod1.pop()
    rod1.pop()
    count = 3
    print(rod1, rod2, rod3)
    # we have to keep track of where the last and current disk are moved from and to
    previous = 0
    current = 0
    future = 0
    present_place = 2
    while rod1 or (rod2 and rod3):  # if two rods are empty at the same time, then we have won the game and stop

        previous = current
        """
                in the cycle we compare the two rods that DON'T have the top two disks (1 and 2)
                and move from the rod with the smallest top disk to the one with the larger one.

                for visual clarity I used the nested ifs
                """

        if present_place == 1:  # the exchange is between rod2 and rod 3
            if rod2 and (not rod3 or rod2[-1] < rod3[-1]):
                rod3.append(rod2.pop())
                current = 2
                future = 3
            else:
                rod2.append(rod3.pop())
                current = 3
                future = 2

        elif present_place == 2:  # the exchange is between rod1 and rod 3
            if rod3 and (not rod1 or rod3[-1] < rod1[-1]):
                rod1.append(rod3.pop())
                current = 3
                future = 1
            else:
                rod3.append(rod1.pop())
                current = 1
                future = 3

        elif present_place == 3:  # the exchange is between rod1 and rod 2
            if rod2 and (not rod1 or rod2[-1] < rod1[-1]):
                rod1.append(rod2.pop())
                current = 2
                future = 1
            else:
                rod2.append(rod1.pop())
                current = 1
                future = 2

        """ 
        if two disks are moved from the same rod (current and previous) one after the other
        then we move the top 2 disks to the rod they came from (current),
        else we move the top 2 disks to the rod that the last disk is moved to (future)
        """
        if previous == current:
            present_place = current
        else:
            present_place = future
        count += 4
    func1(present_place)

    return count


def hanoi(disks):
    "function that returns the count of moves to win a hanoi tower game with the given number of disks"
    return 2**disks - 1


#print(good_hanoi(15))
print(hanoi(50))


def bubble_sort(list_l):
    length = len(list_l)
    i = 0
    while i <= length-1:
        swap = False
        j = 0
        while j <= length - 2 - i:
            if list_l[j] > list_l[j + 1]:
                temp = list_l[j + 1]
                list_l[j + 1] = list_l[j]
                list_l[j] = temp
                swap = True
            j += 1
        if not swap:
            break
        i += 1
    return list_l

print(bubble_sort([5,7,3,8,44,2,8,4,1,4,6]))


def merge(left, right):
    length_left = len(left)
    length_right = len(right)
    l = 0
    r = 0
    temp = []
    while l < length_left and r < length_right:
        if left[l] < right[r]:
            temp.append(left[l])
            l += 1
        elif right[r] <= left[l]:
            temp.append(right[r])
            r += 1
    if l < length_left:
        temp += left[l:]
    elif r < length_right:
        temp += right[r:]
    return temp


def merge_sort(list_l, n):
    if n == 1:
        return list_l

    left = merge_sort(list_l[:n//2], n//2)  # left side
    right = merge_sort(list_l[n//2:], round(n/2))  # right side

    return merge(left, right)

listik = [2,4,6,8,9,1,3,5,7,6,2]
print(merge_sort(listik, len(listik)))

def swap(left, right):
    return right, left

def insert_sort_dumb(list_l):
    length = len(list_l)
    i = 1
    result = [list_l[0]]
    while i<length -1:
        j = len(result) - 1
        if result[j] < list_l[i]:
            result.append(list_l[i])
        else:
            result.append(result[j])
            result[j] = list_l[i]
            j-=1
            while j >=0:
                if result[j]>result[j+1]:
                    result[j], result[j+1] = swap(result[j], result[j+1])
                j-=1
        i+=1
    return result

def insert_sort(list_l):
    length = len(list_l)
    i = 1
    while i<length:
        j = i
        while j>0:
            if list_l[j - 1] > list_l[j]:
                list_l[j - 1], list_l[j] = list_l[j], list_l[j - 1]
            j -= 1
        i+=1
    return list_l


list_q = [2, 4, 6, 8, 9, 1, 3, 5, 7, 6, 2]
list_p = [5, 7, 3, 8, 44, 2, 8, 4, 1, 4, 6]

print("insert sort:")
print(insert_sort(list_q))
print(insert_sort(list_p))







def swap(left, right):
    return right, left



def pivot_choice(l, leng):
    if leng >= 3:
        if l[leng//2] > l[leng-1]:
            l[leng//2], l[leng-1] = l[leng-1], l[leng//2]
        if l[0] > l[leng-1]:
            l[0], l[leng-1] = l[leng-1], l[0]
        if l[0] > l[leng//2]:
            l[0], l[leng//2] = l[leng//2], l[0]
    elif leng == 2:
        if l[0]>l[1]:
            l[0],l[1] = l[1], l[0]

    return l


def quicksort(l, length):
    if length == 0:
        return []
    if length == 1:
        return l
    if length == 2:
        if l[0] > l[1]:
            l[0], l[1] = l[1], l[0]
        return l
    l = pivot_choice(l, length)
    print("pivoted: ", l)

    i = 0
    j = length-1
    p = length//2
    pivot = l[length//2]

    while i<p<j:
        if l[i] > pivot > l[j]:
            l[i], l[j] = l[j], l[i]
            i+=1
            j-=1
        elif l[i] > pivot:
            j -=1
        elif pivot > l[j]:
            i += 1
        else:
            i += 1
            j -= 1
    if i < p:
        pp = p
        while i<pp:
            if l[pp-1] > l[pp]:
                l[pp], l[pp-1] = l[pp-1], l[pp]
            pp -= 1
        p = pp
    elif j > p:
        pp = p
        while pp<j:
            if l[pp] > l[pp+1]:
                l[pp], l[pp+1] = l[pp+1], l[pp]
            pp += 1
        p = pp
    #print("left: ", l[:p-1])
    #print("left: ", l[p:])
    #print(l[:p-1] + l[p:])
    left = quicksort(l[:p], len(l[:p]))
    right = quicksort(l[p:], len(l[p:]))
    #left.append(l[p])

    return left + right



"""
print("Quicksort:")
list_q = [2,4,6,8,9,1,3,5,7,6,2]
list_p = [5,7,3,8,44,2,8,4,1,4,6]
#print(pivot_choice(list_q, len(list_q)))
#print(pivot_choice(list_p, len(list_p)))
print(quicksort(2, 1))
print("result: ", quicksort(list_q, len(list_q)), "\n")

print("result: ",quicksort(list_p, len(list_p)))
"""

def tiaosheng(failed_counter):
    if not failed_counter:
        return 60
    seconds = 0
    jumps = 0
    j = 0
    length = len(failed_counter)
    while seconds < 60:
        if j < length:
            if failed_counter[j] == jumps:
                seconds += 2
                jumps -= 1
                j += 1
        jumps += 1
        seconds += 1

    return jumps

def tiaosheng1(a):
    j, t = 0, 0
    for j in a:
        t += 3
        if j + t > 60:
            return min(j, 60-t+3)
    return 60-t

def tiaosheng2(failed_counter):
    n = 60
    for c in failed_counter:
        if c <= n:
            n -= min(3, n-c)
    return n

def tiaosheng3(fails):
    return 60 - sum(1 for i, f in enumerate(fails) for k in range(3) if 3*i + f + k < 60)














