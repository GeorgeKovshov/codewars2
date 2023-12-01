from collections import deque

#arr = [1,2,3,4]
#arr2 = deque([1,2,3,4])
#arr2.popleft()

#arr2.pop()
#print(arr2)


def custom_fib_rec(arr, indexes, n, i):
    if i == n:
        return arr[n]
    sum = 0
    for ind in indexes:
        sum += arr[ind]
    arr.popleft()
    arr.append(sum)
    return custom_fib_rec(arr, indexes, n-1, i)


def custom_fib_orig(signature, indexes, n):
    if n<0:
        return 0
    i = len(signature) -1
    if n <= i:
        return signature[n]
    arr = deque(signature)

    return custom_fib_rec(arr, indexes, n, i)


def custom_fib(signature, indexes, n):
    if n<0:
        return 0
    i = len(signature)-1
    if n <= i:
        return signature[n]
    arr = deque(signature)
    # let's throw away signature values we'll never use and thus shorten the list traversal on each iteration
    min_ind = i+1
    for ind in indexes:
        min_ind = ind if ind < min_ind else min_ind
    if min_ind < i + 1 and min_ind > 0:
        for j in range(0, len(indexes)):
            indexes[j] -= min_ind
        while min_ind > 0:
            arr.popleft()
            n -= 1
            i -= 1
            min_ind -= 1
    # now the actual fibonacci
    return custom_fib_rec(arr, indexes, n, i)


#print(custom_fib([7, 3, 4, 1], [1, 1], 6))
#print(custom_fib([2, 6], [0, 1, 0], 19))
#print(custom_fib([6, 3, 8], [1, 1, 2, 1, 1], 11))

def custom_fib2(signature, indexes, n):
    fib = deque(signature)
    for _ in range(n):
        fib.append(sum(map(fib.__getitem__, indexes)))
        fib.popleft()
    return fib[0]

count = {
    'a': 1, 'b': 2, 'c': 3, '2': 4,
    'd': 1, 'e': 2, 'f': 3, '3': 4,
    'g': 1, 'h': 2, 'i': 3, '4': 4,
    'j': 1, 'k': 2, 'l': 3, '5': 4,
    'm': 1, 'n': 2, 'o': 3, '6': 4,
    'p': 1, 'q': 2, 'r': 3, 's': 4, '7': 5,
    't': 1, 'u': 2, 'v': 3, '8': 4,
    'w': 1, 'x': 2, 'y': 3, 'z': 4, '9': 5,
    '1': 1, '*': 1, '#': 1, ' ': 1, '0': 2,
}


def presses(phrase):
    summ = 0
    for x in phrase.lower():
        summ += count[x];
    return summ


def presses1(phrase):
    return sum([count[x] for x in phrase.lower()])


print(presses1("HOW R U"))

BUTTONS = [ '1',   'abc2',  'def3',
          'ghi4',  'jkl5',  'mno6',
          'pqrs7', 'tuv8', 'wxyz9',
            '*',   ' 0',    '#'   ]
def presses2(phrase):
    return sum(1 + button.find(c) for c in phrase.lower() for button in BUTTONS if c in button)

def runShell(boxNr):
    # G00D LUCK!
    if boxNr == 1:
        return "help"
    elif boxNr == 2:
        return "help"
    else:
        return "help"


"""
Available commands: help, echo, cat, exit, ls -l, cd, pwd, su, man, whoami

su
        #Allows you to change user, syntax: su 'user' 'password'
        #For example su root rootpassword makes you root

cat
Shows content of a file, but works here only with files in the current directory
For example cat /etc/passwd is not possible, because it's an absolute path
Normally you can't cat passwd, just saying

Echo prints something into the console
With '>' you can change the output stream to a file. Here only local files work
For example echo 'test' > /etc/passwd is not possible, because it's an absolute path
Normally you can't write anything to passwd, just saying

cd
Changes directory
Here only absolute paths work
For example cd /etc works, but cd etc doesn't work
In /etc there are important files, just saying

"pwd; ls -l; cd /etc; pwd; ls -l; cat passwd"
root:x:0:0::/root:/bin/bash

ls -l
Lists all files of the current directory, and shows permissions
Maybe you can use it to detect wrongly set permissions on important files like passwd


"""


def is_isogram(string):
    arr = []
    for s in string:
        if s.lower() in arr:
            return False
        arr.append(s.lower())
    return True

def is_isogram2(string):
    return len(string) == len(set(string.lower()))



def cut_the_ropes(arr):
    length = len(arr)
    m = min(arr)
    result = []
    while m != 0:
        m1 = 0
        count = 0
        for i in range(length):
            if arr[i] != 0:
                count += 1
                arr[i] -= m
                if m1 == 0 or (arr[i] < m1 and arr[i] != 0):
                    m1 = arr[i]
        m = m1
        result.append(count)
    return result


def cut_the_ropes2(a):
    if not a:
        return []
    m = min(a)
    return [len(a)] + cut_the_ropes2([x-m for x in a if x > m])

#print(cut_the_ropes([3, 3, 2, 9, 7]))
#print(cut_the_ropes([1, 2, 3, 4, 3, 3, 2, 1]))


def freed_prisoners(prison):
    current = True
    count = -1
    for p in prison:
        if p == current:
            current = not current
            count += 1
    return count


class Block:
    width = int
    length = int
    height = int

    def __init__(self, arr):
        self.width = arr[0]
        self.length = arr[1]
        self.height = arr[2]

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.height * self.length * self.width

    def get_surface_area(self):
        return 2 * self.height * self.length + 2 * self.width * self.length + 2 * self.height * self.width


import math


class Sphere(object):
    radius = float
    mass = float

    def __init__(self, rad, mass):
        self.radius = rad
        self.mass = float

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(self.radius * self.radius * self.radius * math.pi * 4 / 3, 5)

    def get_surface_area(self):
        return round(self.radius * self.radius * math.pi * 4, 5)

    def get_density(self):
        return round(self.get_mass() / self.get_volume(), 5)



class Multip:
    """
    arr = []
    permute = []
    result = []
    max_permute = int
    amount_permute = int
    hash_dict = {}
    length = int
    """

    def __init__(self, num):
        self.arr = []
        self.permute = []
        self.result = []
        length = 0
        self.amount_permute = 0
        self.max_permute = 0
        zero_present = False
        while num >= 1:
            if num % 10 == 0:
                zero_present = True
            self.arr.append(num % 10)
            num = num // 10
            length += 1
        self.length = length
        if zero_present:
            self.amount_permute -= 1

    def count_permutations_helper(self, split_len, length):
        result = 1
        while split_len > 0:
            result *= length
            length -= 1
            split_len -= 1
        return result

    def count_permutations(self, num):
        split = {}
        length = 0
        split_len = -1
        while num >= 1:
            if num % 10 not in split:
                split[num % 10] = 0
                split_len += 1
            split[num % 10] += 1
            num = num // 10
            length += 1
        result = self.count_permutations_helper(split_len, length)
        if 0 in split:
            result -= (self.count_permutations_helper(split_len - 1, length - 1)) * split[0]
        return result

    def count_permutations_helper1(self, split):
        """start the formula"""
        result = 1
        divide = []
        factori = 0
        product = 1
        division = 1
        for key in split:
            factori += split[key]
            if split[key] > 1:
                divide.append(split[key])
        while factori > 0:
            product *= factori
            factori -= 1
        for x in divide:
            pro = 1
            while x > 0:
                pro *= x
                x -= 1
            division *= pro
        result = product / division
        """end the formula"""
        return result

    def count_permutations1(self, num):
        """the good one"""
        split = {}
        length = 0
        split_len = -1
        while num >= 1:
            if num % 10 not in split:
                split[num % 10] = 0
                split_len += 1
            split[num % 10] += 1
            num = num // 10
            length += 1
        result = self.count_permutations_helper1(split)
        if 0 in split:
            split[0] -= 1
            result -= self.count_permutations_helper1(split)
        return result


    def recursive_find1(self, current_num, index):
        """the good one"""
        if index >= self.length:
            return
        for i in range(index, self.length):
            num = current_num * 10 + self.arr[i]
            if num in self.permute:
                continue
            self.permute.append(num)
            if num % 3 == 0:
                self.result.append(num)
                self.amount_permute += self.count_permutations1(num)
                self.max_permute = max(self.max_permute, num)
            self.recursive_find1(num, i + 1)
        return


    def recursive_find2(self, avail_ar, permuted_ar, power):
        """the slow one"""
        length_avail = len(avail_ar)
        if length_avail < 1:
            return
        length_permuted = len(permuted_ar)
        start = 3
        if power == 0:
            start = 0
        for i in range(length_avail):
            for j in range(start, length_permuted):
                num = avail_ar[i] + permuted_ar[j] * 10

                if num in self.hash_dict[power] or num / pow(10, power) < 1:
                    continue
                self.hash_dict[power].append(num)
                if num % 3 == 0:
                    self.result.append(num)
                self.recursive_find2(avail_ar[:i] + avail_ar[i+1:], permuted_ar + [num], power + 1)

        return

    def recursive_start(self):
        #self.recursive_find2(self.arr, [0,0,0], 0)
        self.arr = sorted(self.arr, reverse=True)
        self.recursive_find1(0, 0)


    def reset(self):
        self.arr.clear()
        self.permute.clear()
        self.result.clear()
        self.max_permute = 0
        self.amount_permute = 0
        self.length = 0



def find_mult_3(num):
    arr = Multip(num)

    #arr.find(3)
    arr.recursive_start()
    print(arr.arr)
    #arr.recursive_find1(arr.arr)
    print(arr.max_permute, arr.amount_permute)
    print(sorted(arr.result))




#print(find_mult_3(362))
#print(find_mult_3(6063))
#print(find_mult_3(7766553322))

from itertools import permutations


def find_mult_3_2(num):
    num_list = tuple(map(int, str(num)))

    poss = set()
    for i in range(1, len(num_list) + 1):
        poss |= set(permutations(num_list, i))

    res = set()
    for p in poss:
        if p[0] != 0 and sum(p) % 3 == 0:
            res.add(p)

    res = [sum(x * 10 ** n for n, x in enumerate(p[::-1])) for p in res]
    return [len(res), max(res)]

def find_mult_3_3(num):
  ls = []
  for i in range(1, len(str(num))+1):
    for j in set(permutations(str(num), i)):
      ls.append(int(''.join(j)))
  ls = set(ls)
  solve = [x for x in ls if x != 0 and x % 3 == 0]
  return [len(solve), max(solve)]

#ar = [1, 2, 3, 4, 5, 6, 7, 8]
#num = 2
#print(ar + [num])
#i = len(ar)-1
#print(ar[:i] + ar[i+1:])

def count_permutations_helper(split_len, length):
    result = 1
    while split_len > 0:
        result *= length
        length -= 1
        split_len -= 1
    return result

def count_permutations(num):
    split = {}
    length = 0
    split_len = -1
    while num >= 1:
        if num % 10 not in split:
            split[num % 10] = 0
            split_len += 1
        split[num % 10] += 1
        num = num // 10
        length += 1
    result = count_permutations_helper(split_len, length)
    if 0 in split:
        result -= (count_permutations_helper(split_len - 1, length - 1)) * split[0]
    return result

def count_permutations_helper1(split):
    """start the formula"""
    result = 1
    divide = []
    factori = 0
    product = 1
    division = 1
    for key in split:
        factori += split[key]
        if split[key] > 1:
            divide.append(split[key])
    while factori > 0:
        product *= factori
        factori -= 1
    for x in divide:
        pro = 1
        while x > 0:
            pro *= x
            x -= 1
        division *= pro
    result = product / division

    return result



def count_permutations1(num):
    split = {}
    length = 0
    split_len = -1
    while num >= 1:
        if num % 10 not in split:
            split[num % 10] = 0
            split_len += 1
        split[num % 10] += 1
        num = num // 10
        length += 1
    result = count_permutations_helper1(split)
    if 0 in split:
        split[0] -= 1
        result -= count_permutations_helper1(split)
    return result


#print(count_permutations1(120))
#for x in count_permutations1(360):
    #print(x)


def two_sum(numbers, target):
    dicts = {}
    for i in range(len(numbers)):
        if numbers[i] in dicts:
            return (dicts[numbers[i]],i)
        dicts[target - numbers[i]] = i
    return []


def find_uniq(arr):
    dict = {}
    for x in arr:
        if x not in dict:
            dict[x] = 0
        dict[x] += 1
    for y in dict:
        if dict[y] == 1:
            return y
    return ""


def find_uniq2(arr):
    dict = {}
    i = 0
    for line in arr:
        tmp = set([x for x in line.lower() if x != " "])
        for y in tmp:
            if y not in dict:
                dict[y] = i
            else:
                dict[y] = -1
        i += 1
    i = 0
    for d in dict:
        if dict[d] != -1:
            return arr[dict[d]]
    return ""


def remove_smallest(numbers):
    i = len(numbers) - 1
    if i <= 0:
        return []
    min = [i, numbers[i]]
    i -= 1
    while i>=0:
        if min[1] >= numbers[i]:
            min = [i, numbers[i]]
        i -= 1
    return numbers[:min[0]] + numbers[min[0]+1:]


def remove_smallest2(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a

def sort_odd_indeces(source_array):
    i = len(source_array)
    t = 0
    change = True
    while i>0 and change:
        change = False
        while t + 2 < i:
            if source_array[t] > source_array[t + 2]:
                tmp = source_array[t]
                source_array[t] = source_array[t + 2]
                source_array[t + 2] = tmp
                change = True
            t += 2
        i -= 2;
        t = 0
    return source_array


def sort_odd_array(arr):
    i = 0
    j = len(arr)
    last = arr[0]
    for x in arr:
        if x % 2 != 0:
            last = x
            break
        i += 1
    if last % 2 == 0:
        return arr

    while i + 1 < j:
        if arr[i + 1] < last and arr[i+1] % 2 != 0:
            t = i
            ind = i + 1
            while t >= 0:
                if arr[t] % 2 != 0 and arr[ind] < arr[t]:
                    tmp = arr[ind]
                    arr[ind] = arr[t]
                    arr[t] = tmp
                    ind = t
                elif arr[t] % 2 != 0:
                    break
                t -= 1
            last = arr[i + 1]
        elif arr[i+1] % 2 != 0:
            last = arr[i + 1]
        i += 1

    return arr


def sort_odd_array2(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


#print(sort_odd_array([5, 3, 2, 8, 1, 4]))
print(sort_odd_array([1, 111, 11, 11, 2, 1, 5, 0]))

#[1, 111, 11, 11, 2, 1, 5, 0] should equal
#[1, 1, 5, 11, 2, 11, 111, 0]

#[-49, -27, -5, 7, 32, 22, 33, 39, -44, 13] should equal
#[-49, -27, -5, 7, 32, 22, 13, 33, -44, 39]


def order(sentence):
    if sentence == "":
        return ""
    arr = sentence.split()
    result = ["", "", "", "", "", "", "", "", ""]
    for word in arr:
        for letter in word:
            if letter.isdigit():
                result[int(letter) - 1] = word
                break
    print(result)
    res = " ".join([x for x in result if x != ""])
    return res


def arrange(strng):
    words = strng.split()
    lengths = []
    for word in words:
        lengths.append(len(word))
    print("lengths", len(lengths), " words", len(words))

    result = []
    i = 0
    word_amount = len(words)
    odd = True
    while i < word_amount - 1:
        if lengths[i] <= lengths[i + 1] and odd:
            result.append(words[i].lower())
        elif lengths[i] >= lengths[i + 1] and not odd:
            result.append(words[i].upper())
        else:
            if odd:
                result.append(words[i + 1].lower())
            else:
                result.append(words[i + 1].upper())
            words[i + 1] = words[i]
            lengths[i + 1] = lengths[i]
        i += 1
        odd = not odd
    if (word_amount > 0):
        if odd:
            result.append(words[-1].lower())
        else:
            result.append(words[-1].upper())
    return " ".join([x for x in result])

def arrange2(strng):
    words = strng.split()
    for i in range(len(words)):
        words[i:i+2] = sorted(words[i:i+2], key=len, reverse=i%2)
        words[i] = words[i].upper() if i%2 else words[i].lower()
    return ' '.join(words)


def split_integer(num, parts):
    divider = int(num / parts)
    result = [divider] * parts
    sum = int(divider * parts)
    i = len(result) - 1
    while sum != num and i>=0:
        if sum > num:
            result[i] -= 1
            sum -= 1
        else:
            result[i] += 1
            sum += 1
        i-=1
    return result


def pop_blocks(lst):
    result = []
    found = False
    for i in range(len(lst)-1):
        if lst[i] != lst[i+1] and not found:
            result.append(lst[i])
        elif lst[i] != lst[i+1] and found:
            result = result + lst[i+1:]
            break;
        else:
            found = True
    if found:
        return pop_blocks(result)
    else:
        if len(lst) > 0:
            result.append(lst[-1])
        return result

#print(153//10)
#var = 153
#print([int(x)**3 for x in list(str(var))])

# d = direction, v = values array, c = number to search
# return None in case of value not found
def cycle(d, v, c):
    for i in range(len(v)):
        if v[i] == c:
            if  i + d < 0:
                return v[len(v)+d]
            elif i + d >= len(v):
                return v[0]
            else:
                return v[i+d]
    return None
'''
def locate_entrance(office: List[str]) -> Tuple[int, int]:
    for i in range(len(office)):
        for j in range(len(office[i])):
            if office[i][j] == '.':
                if i == len(office) - 1 or i == 0 or j==0 or j==len(office[i])-1:
                    return(j,i)
                elif len(office[i-1])<=j or len(office[i+1])<=j:
                    return(j,i)
                elif office[i-1][j] == " " or office[i+1][j] == " " or office[i][j-1] == " " or office[i][j+1] == " ":
                    return(j,i)
    return ("","")
'''
def tops(msg):
    i = 1
    length = len(msg)
    addition = 2
    result = []
    while i < length:
        result.append(msg[i])
        #result = msg[i] + result
        i += addition * 2 + 1
        addition += 2
    return "".join(result[::-1])


def tops2(msg):
    i = 2
    length = len(msg)
    current = 2
    addition = 2
    result = []
    while i < length:
        result.append(msg[i:(i+current)])
        i += current
        addition += 3
        i += addition
        current += 1
    return "".join(result[::-1])


def alphabet_war(fight):
    dict = {
        'w' : 4,
        'p' : 3,
        'b' : 2,
        's' : 1,
        'm' : -4,
        'q' : -3,
        'd' : -2,
        'z' : -1,
    }
    result = 0
    for fighter in fight:
        if fighter in dict:
            result += dict[fighter]
    if result > 0:
        return "Left side wins!"
    elif result < 0:
        return "Right side wins!"
    else:
        return "Let's fight again!"


def alphabet_war2(fight):
    dict = {
        'w': 4,
        'p': 3,
        'b': 2,
        's': 1,
        'm': -4,
        'q': -3,
        'd': -2,
        'z': -1,
    }
    length = len(fight)
    arr = list(fight)
    for i in range(length):
        if fight[i] == '*':
            if i < length - 1:
                arr[i + 1] = '_'
            if i > 0:
                arr[i - 1] = '_'
    result = 0
    for fighter in arr:
        if fighter in dict:
            result += dict[fighter]

    if result > 0:
        return "Left side wins!"
    elif result < 0:
        return "Right side wins!"
    else:
        return "Let's fight again!"


def alphabet_war3(reinforces, airstrikes):
    depth = len(airstrikes)
    length = 0
    for x in airstrikes:
        length = len(x) if len(x) > length else length
    bombings = [0] * length
    i = 0
    while i < depth:
        for j in range(0, len(airstrikes[i])):
            if airstrikes[i][j] == '*':
                if j == 0 or airstrikes[i][j - 1] != '*':
                    bombings[j] += 1
                if j < length - 1:
                    bombings[j + 1] += 1
        i += 1

    result = []
    for j in range(length):
        result.append(reinforces[bombings[j]][j])
    return "".join(result)

def count_sel(lst):
    # loop through list to make a dictionary
    dict = {}
    count_all = 0
    count_different = 0
    maximum = 0
    for val in lst:
        if val not in dict:
            dict[val] = 0
            count_different += 1
        if dict[val] + 1 >= maximum:
            maximum = dict[val] + 1
        dict[val] += 1
        count_all += 1
    # loop through dictionary to get all data
    count_single = 0
    array_maximum = []
    for key in dict:
        if dict[key] == 1:
            count_single += 1
        if dict[key] == maximum:
            array_maximum.append(key)
    array_maximum.sort()
    return [count_all, count_different, count_single, [array_maximum, maximum]]

def find_inner_braces(s):
    length = len(s)
    i = 0
    current_braces = [-1,-1]
    while i < length:
        if s[i] == '(':
            current_braces[0] = i
        if s[i] == ')':
            current_braces[1] = i
            break
        i += 1
    #print(s[current_braces[0]:current_braces[1]+1])
    return current_braces


def solve_equation(equation):
    negation = {
        'T': 'F',
        'U': 'U',
        'F': 'T'
    }
    arr = equation.strip().split()
    previous = ""
    i = 0
    print(arr)
    length = len(arr)
    while i < length:
        if arr[i] == "not":
            arr[i+1] = negation[arr[i+1]]
            arr[i] = ""
        i += 1

    print(" ".join(arr))
    i = 0
    while i < length:
        if arr[i] == "and":
            j = 1
            while arr[i+j] == "":
                j += 1
            z = -1
            while arr[i+z] == "":
                z -= 1
            if arr[i+z] == 'T' and arr[i+j] == 'T':
                arr[i] = 'T'
            elif (arr[i+z] == 'T' and arr[i+j] == 'U') or (arr[i+z] == 'U' and arr[i+j] == 'T') or (arr[i+z] == 'U' and arr[i+j] == 'U'):
                arr[i] = 'U'
            else:
                arr[i] = 'F'
            arr[i + z] = ""
            arr[i + j] = ""
        i += 1
    print(" ".join(arr))
    i = 0
    while i < length:
        if arr[i] == "xor":
            j = 1
            while arr[i + j] == "":
                j += 1
            z = -1
            while arr[i + z] == "":
                z -= 1
            if (arr[i + z] == 'T' and arr[i + j] == 'T') or (arr[i + z] == 'F' and arr[i + j] == 'F'):
                arr[i] = 'F'
            elif (arr[i + z] == 'T' and arr[i + j] == 'F') or (arr[i + z] == 'F' and arr[i + j] == 'T'):
                arr[i] = 'T'
            else:
                arr[i] = 'U'
            arr[i + z] = ""
            arr[i + j] = ""
        i += 1
    print(" ".join(arr))
    i = 0
    while i < length:
        if arr[i] == "or":
            j = 1
            while arr[i + j] == "":
                j += 1
            z = -1
            while arr[i + z] == "":
                z -= 1
            if arr[i + z] == 'F' and arr[i + j] == 'F':
                arr[i] = 'F'
            elif (arr[i + z] == 'F' and arr[i + j] == 'U') or (arr[i + z] == 'U' and arr[i + j] == 'F') or (
                    arr[i + z] == 'U' and arr[i + j] == 'U'):
                arr[i] = 'U'
            else:
                arr[i] = 'T'
            arr[i + z] = ""
            arr[i + j] = ""
        i += 1
    print(" ".join(arr))
    return "".join(arr).strip()


def threevl(s):
    braces_indeces = find_inner_braces(s)
    while braces_indeces[0] != -1 and braces_indeces[1] != -1:
        tmp = solve_equation(s[braces_indeces[0]+1:braces_indeces[1]])
        s = s[:braces_indeces[0]] + tmp + s[braces_indeces[1] + 1:]
        braces_indeces = find_inner_braces(s)
    return solve_equation(s)


#print(find_inner_braces("(not T or U) and (not U or T)"))
#print(threevl("not T or U"))


class Partitions:
    def __init__(self, n):
        self.partition_list = []
        self.max_score = []
        self.min_score = []
        num = n
        i = 2
        result = []
        while i < n/2 + 2 and num > 1:
            if num % i == 0:
                result.append(i)
                num = num // i
                i -= 1
            i += 1
        if i >= n/2+1:
            self.partition_list.append("It is a prime number")
            return
        result.sort(reverse=True)
        self.max_score.append(result)
        self.min_score.append(result)
        self.max_score.append(self.calculate_score(result))
        self.min_score.append(self.max_score[1])
        self.partition_list.append(result)

    def calculate_score(self, arr):
        count_dict = {}
        length = 0
        for key in arr:
            if key not in count_dict:
                count_dict[key] = 0
            count_dict[key] += 1
            length += 1
        result = 0
        for key in count_dict:
            result += key ** count_dict[key]
        return result * length


    def find_partitions_rec(self, part):
        i = 0
        length = len(part)
        while i < length-1:
            j = i + 1
            while j < length:
                tmp = part[:i] + part[i+1:j] + part[j+1:] + [part[i] * part[j]]
                tmp.sort(reverse=True)
                if tmp not in self.partition_list and len(tmp) > 1:
                    score = self.calculate_score(tmp)

                    if score > self.max_score[1]:
                        self.max_score[0] = tmp
                        self.max_score[1] = score
                    elif score < self.min_score[1]:
                        self.min_score[0] = tmp
                        self.min_score[1] = score

                    self.partition_list.append(tmp)
                    self.find_partitions_rec(tmp)
                j += 1
            i += 1

    def initiate_find_partitions(self):
        self.find_partitions_rec(self.partition_list[0])


def find_spec_prod_part(n, com):
    part = Partitions(n)
    if part.partition_list[0] == "It is a prime number":
        return "It is a prime number"
    part.initiate_find_partitions()
    return part.min_score if com == "min" else part.max_score


#print(find_spec_prod_part(1416, "max"))

def rec_spiral():
    return

def spiralize(size):
    field = [[1]*size]
    for i in range(size-2):
        field.append(([0]*(size-1) + [1]))
    field.append([1] * size)
    i = size - 1
    j = 0
    moved = True
    while moved:
        moved = False
        count = 0
        while field[i-2][j] != 1:
            field[i-1][j] = 1
            i -= 1
            count += 1
            moved = True
        if count == 1:
            return field

        count = 0
        while field[i][j+2] != 1:
            field[i][j+1] = 1
            j += 1
            count += 1
            moved = True
        if count == 1:
            return field

        count = 0
        while field[i+2][j] != 1:
            field[i+1][j] = 1
            i += 1
            count += 1
            moved = True
        if count == 1:
            return field

        count = 0
        while field[i][j-2] != 1:
            field[i][j-1] = 1
            j -= 1
            count += 1
            moved = True
        if count == 1:
            return field

    return field

'''
spiral = spiralize(5)
for s in spiral:
    print(s)
'''

def get_digits(num):
    result = []
    while num >= 1:
        result.append(num % 10)
        num = num // 10
    return result

def get_score(num):
    result = num % 10
    num = num // 10
    previous = result
    while num >= 1:
        current = num % 10
        if current > previous:
            result -= current ** (abs(current - previous))
        else:
            result += current ** (abs(current - previous))
        previous = current
        num = num // 10
    return result


def prev_next(n):
    low = n - 1
    high = n + 1
    left = -1
    right = -1
    if n > 100:
        while low >= 100:
            if get_score(low) == 0:
                left = low
                break
            low -= 1
    if n < 1000000:
        while high <= 1500000:
            if get_score(high) == 0:
                right = high
                break
            high += 1

    if get_score(n) == 0:
        if left == -1 and right == -1:
            return [n]
        elif left == -1:
            return [n, right]
        elif right == -1:
            return [left, n]
        return [left, n, right]
    else:
        if left == -1 and right == -1:
            return []
        elif left == -1:
            return [right]
        elif right == -1:
            return [left]
        return [left, right]


#print(get_score(186599))
#print(prev_next(150))


class Solution:
    def __init__(self, shape):
        # shape = shape.replace(" ", "0")
        s = shape.splitlines()
        # print(s)
        list_shape = []
        self.width = 0
        for line in s:
            list_line = []
            for i in range(len(line)):
                list_line.append(line[i])
            if len(list_line) > self.width:
                self.width = len(list_line)
            list_shape = list_shape + [list_line]
        self.list_shape = list_shape
        self.depth = len(list_shape)
        for i in range(self.depth):
            if len(self.list_shape[i]) < self.width:
                self.list_shape[i] = self.list_shape[i] + [' '] * (self.width - len(self.list_shape[i]))
        self.vertices = {}
        self.fake_vertices = []
        self.cut_figures = []
        # for x in self.list_shape:
        # print("line: ", x, " width:", len(x))
        # self.width = len(list_shape[1])
        # print(self.width)
        # for x in list_shape:
        # print(x)

    def figure_mapper(self, i, j, num, open_border):
        if not open_border:
            self.list_shape[i][j] = num
            # checking for holes
            if i == 0 or i == self.depth - 1 or j == 0 or j == self.width - 1:
                open_border = True
                self.fake_vertices.append(num)
                self.figure_mapper(i, j, num, open_border)
                return

            if i >= 1 and self.list_shape[i - 1][j] == ' ':
                self.figure_mapper(i - 1, j, num, open_border)
            if i < self.depth - 1 and self.list_shape[i + 1][j] == ' ':
                self.figure_mapper(i + 1, j, num, open_border)
            if j >= 1 and self.list_shape[i][j - 1] == ' ':
                self.figure_mapper(i, j - 1, num, open_border)
            if j < self.width - 1 and self.list_shape[i][j + 1] == ' ':
                self.figure_mapper(i, j + 1, num, open_border)
        else:
            self.list_shape[i][j] = '0'
            if i >= 1 and self.list_shape[i - 1][j] in [' ', num]:
                self.figure_mapper(i - 1, j, num, open_border)
            if i < self.depth - 1 and self.list_shape[i + 1][j] in [' ', num]:
                self.figure_mapper(i + 1, j, num, open_border)
            if j >= 1 and self.list_shape[i][j - 1] in [' ', num]:
                self.figure_mapper(i, j - 1, num, open_border)
            if j < self.width - 1 and self.list_shape[i][j + 1] in [' ', num]:
                self.figure_mapper(i, j + 1, num, open_border)
        # store the coordinates of figure in graph
        self.vertices[num][0] = i if i < self.vertices[num][0] else self.vertices[num][0]
        self.vertices[num][1] = i if i > self.vertices[num][1] else self.vertices[num][1]
        self.vertices[num][2] = j if j < self.vertices[num][2] else self.vertices[num][2]
        self.vertices[num][3] = j if j > self.vertices[num][3] else self.vertices[num][3]
        return

    def overview_traversal(self):
        num = 1
        for i in range(self.depth):
            for j in range(self.width):
                if self.list_shape[i][j] == ' ':
                    self.vertices[str(num)] = [1000, -1, 1000, -1]  # [min i, max i, min j, max j]
                    self.figure_mapper(i, j, str(num), False)
                    num += 1
        return

    def cut_out_figure(self, num):
        coord = self.vertices[num]
        tmp = []
        for i in range(coord[0] - 1, coord[1] + 2):
            tmp.append(self.list_shape[i][coord[2] - 1:coord[3] + 2])

        depth = len(tmp) - 1
        width = len(tmp[0]) - 1
        for i in range(depth + 1):
            for j in range(width + 1):
                if tmp[i][j] not in ['-', '+', '|', num]:
                    tmp[i][j] = ' '
                elif tmp[i][j] == '-':
                    if (i > 0 and tmp[i - 1][j] == num) or (i < depth and tmp[i + 1][j] == num):
                        tmp[i][j] = '-'
                    else:
                        tmp[i][j] = ' '
                elif tmp[i][j] == '|':
                    if (j > 0 and tmp[i][j - 1] == num) or (j < width and tmp[i][j + 1] == num):
                        tmp[i][j] = '|'
                    else:
                        tmp[i][j] = ' '
                elif tmp[i][j] == '+':
                    touches_num = False
                    if i > 0 and j > 0:
                        touches_num = True if tmp[i - 1][j - 1] == num else touches_num
                    if i > 0 and j < width:
                        touches_num = True if tmp[i - 1][j + 1] == num else touches_num
                    if i < depth and j > 0:
                        touches_num = True if tmp[i + 1][j - 1] == num else touches_num
                    if i < depth and j < width:
                        touches_num = True if tmp[i + 1][j + 1] == num else touches_num

                    if i > 0:
                        touches_num = True if tmp[i - 1][j] == num else touches_num
                    if i < depth:
                        touches_num = True if tmp[i + 1][j] == num else touches_num
                    if j > 0:
                        touches_num = True if tmp[i][j - 1] == num else touches_num
                    if j < width:
                        touches_num = True if tmp[i][j + 1] == num else touches_num

                    if not touches_num:
                        tmp[i][j] = ' '
        for i in range(depth + 1):
            for j in range(width + 1):
                if tmp[i][j] == num:
                    tmp[i][j] = ' '
                elif tmp[i][j] == '+':

                    if i < depth and i > 0 and tmp[i + 1][j] in ['|', '+'] and tmp[i - 1][j] in ['|', '+']:
                        tmp[i][j] = '|'
                    elif j < width and j > 0 and tmp[i][j + 1] in ['-', '+'] and tmp[i][j - 1] in ['-', '+']:
                        tmp[i][j] = '-'

                    if i < depth and i > 0 and j < width and j > 0:
                        count = 0
                        if tmp[i + 1][j] in ['|', '+']:
                            count += 1
                        if tmp[i - 1][j] in ['|', '+']:
                            count += 1
                        if tmp[i][j + 1] in ['-', '+']:
                            count += 1
                        if tmp[i][j - 1] in ['-', '+']:
                            count += 1
                        if count >= 3:
                            tmp[i][j] = '+'

        result = "\n".join([("".join(x)).rstrip() for x in tmp])
        self.cut_figures.append(result)
        # for x in tmp:

        # print(x)
        # print(result)
        # return

    def make_figures_list(self):
        for y in self.vertices:
            if y not in self.fake_vertices:
                self.cut_out_figure(y)
                # print("+++++++++++++++")
                # print(y, ": ", self.vertices[y])
        return

    def print(self):
        for x in self.list_shape:
            print(x, self.width)
        print("____")
        for y in self.vertices:
            if y not in self.fake_vertices:
                print(y, ": ", self.vertices[y])


def break_pieces(shape):
    # shape = shape.replace(" ", "0")
    s = shape.splitlines()
    # print(s)
    '''
    list_shape = []
    for line in s:
        list_line = []
        for i in range(len(line)):
            list_line.append(line[i])
        list_shape.append([list_line])

    '''
    for x in s:
        print(x)

    result = Solution(shape)
    result.overview_traversal()
    # result.print()
    result.make_figures_list()

    return result.cut_figures

# uncomment next line if you prefer raw error messages
# raw_errors = True
def test_Immortal2():
    result = []
    first_sum = 0
    other_sum = 0
    length = 16
    modifier = 1

    for i in range(16):
        #hor_modifier = modifier
        other_sum += i
        line = []
        for j in range(length):
            #if i % 8 == 0 and j % 8 == 0:
            line.append(i ^ j)
            first_sum += i ^ j
            if (j+1) % 4 == 0:
                line.append("|")
                #hor_modifier *= 2
        if line:
            result.append(line)
        if (i+1) % 4 == 0:
            result.append(["-"] * length)
            #modifier *= 2

    whole = 0
    for x in result:
        #whole += sum(x)
        #whole += x.count(319)
        print(x)
    #print(whole)
    print(first_sum)
    print(other_sum * length)


def test_Immortal():
    print("--------------")
    result = []
    first_sum = 0
    other_sum = 0
    length = 16
    modifier = 1
    for i in range(7):
        #hor_modifier = modifier
        other_sum += i
        line = []
        for j in range(length):
            #if i % 8 == 0 and j % 8 == 0:
            line.append(i ^ j)
            first_sum += i ^ j
            if (j+1) % 4 == 0:
                line.append("|")
                #hor_modifier *= 2
        if line:
            result.append(line)
        if (i+1) % 4 == 0:
            result.append(["-"] * length)
            #modifier *= 2

    whole = 0
    for x in result:
        #whole += sum(x)
        #whole += x.count(319)
        print(x)
    #print(whole)
    print(first_sum)
    print(other_sum * length)
#test_Immortal()
#print(32 * 8)
#print(256 * 256)
#print(whole)
#print(1 ^ 3)
#print(2208 - 960)
#print(1920 -224)

#print(28827050410* 35165045587)

class Solution2:
    def __init__(self, shape):
        # shape = shape.replace(" ", "0")
        s = shape.splitlines()
        # print(s)
        list_shape = []
        self.width = 0
        for line in s:
            list_line = []
            for i in range(len(line)):
                list_line.append(line[i])
            if len(list_line) > self.width:
                self.width = len(list_line)
            list_shape = list_shape + [list_line]
        self.list_shape = list_shape
        self.depth = len(list_shape)
        for i in range(self.depth):
            if len(self.list_shape[i]) < self.width:
                self.list_shape[i] = self.list_shape[i] + [' '] * (self.width - len(self.list_shape[i]))
        self.vertices = {}
        self.small_vertices = {}
        self.fake_vertices = []
        self.cut_figures = []
        # for x in self.list_shape:
        # print("line: ", x, " width:", len(x))
        # self.width = len(list_shape[1])
        # print(self.width)
        # for x in list_shape:
        # print(x)

    def figure_mapper(self, i, j, num, open_border):
        if not open_border:
            self.list_shape[i][j] = num
            # checking for holes
            if i == 0 or i == self.depth - 1 or j == 0 or j == self.width - 1:
                open_border = True
                self.fake_vertices.append(num)
                self.figure_mapper(i, j, num, open_border)
                return

            if i >= 1 and self.list_shape[i - 1][j] == ' ':
                self.figure_mapper(i - 1, j, num, open_border)
            if i < self.depth - 1 and self.list_shape[i + 1][j] == ' ':
                self.figure_mapper(i + 1, j, num, open_border)
            if j >= 1 and self.list_shape[i][j - 1] == ' ':
                self.figure_mapper(i, j - 1, num, open_border)
            if j < self.width - 1 and self.list_shape[i][j + 1] == ' ':
                self.figure_mapper(i, j + 1, num, open_border)
        else:
            self.list_shape[i][j] = '0'
            if i >= 1 and self.list_shape[i - 1][j] in [' ', num]:
                self.figure_mapper(i - 1, j, num, open_border)
            if i < self.depth - 1 and self.list_shape[i + 1][j] in [' ', num]:
                self.figure_mapper(i + 1, j, num, open_border)
            if j >= 1 and self.list_shape[i][j - 1] in [' ', num]:
                self.figure_mapper(i, j - 1, num, open_border)
            if j < self.width - 1 and self.list_shape[i][j + 1] in [' ', num]:
                self.figure_mapper(i, j + 1, num, open_border)
        # store the coordinates of figure in graph
        self.vertices[num][0] = i if i < self.vertices[num][0] else self.vertices[num][0]
        self.vertices[num][1] = i if i > self.vertices[num][1] else self.vertices[num][1]
        self.vertices[num][2] = j if j < self.vertices[num][2] else self.vertices[num][2]
        self.vertices[num][3] = j if j > self.vertices[num][3] else self.vertices[num][3]
        return

    def small_figure_1(self, i, j, num):
        coords = [i, i, j - 1, j]  # min i, max i, min j, max j
        while coords[0] > 0 and self.list_shape[coords[0]][j] == '|':
            self.list_shape[coords[0]][j] = '/'
            self.list_shape[coords[0]][j - 1] = '/'
            coords[0] -= 1
        self.list_shape[i][j] = '|'
        while coords[1] < self.depth and self.list_shape[coords[1]][j] == '|':
            self.list_shape[coords[1]][j] = '/'
            self.list_shape[coords[1]][j - 1] = '/'
            coords[1] += 1
        self.small_vertices[num] = coords

    def small_figure_2(self, i, j, num):
        coords = [i - 1, i, j - 1, j]  # min i, max i, min j, max j
        while coords[2] > 0 and self.list_shape[i][coords[2]] == '-':
            self.list_shape[i][coords[2]] = '_'
            self.list_shape[i - 1][coords[2]] = '_'
            coords[2] -= 1
        self.list_shape[i][j] = '-'
        while coords[3] < self.width and self.list_shape[i][coords[3]] == '-':
            self.list_shape[i][coords[3]] = '_'
            self.list_shape[i - 1][coords[3]] = '_'
            coords[3] += 1
        self.small_vertices[num] = coords

    def overview_traversal(self):
        num = 1
        small_num = 1
        up = "0"
        for i in range(self.depth):
            left = "0"
            for j in range(self.width):
                if self.list_shape[i][j] == ' ':
                    self.vertices[str(num)] = [1000, -1, 1000, -1]  # [min i, max i, min j, max j]
                    self.figure_mapper(i, j, str(num), False)
                    num += 1
                elif self.list_shape[i][j] == '|' and left == "|":
                    self.small_figure_1(i, j, str(small_num))
                    small_num += 1
                elif self.list_shape[i][j] == '-' and i > 0 and self.list_shape[i - 1][j] == '-':
                    self.small_figure_2(i, j, str(small_num))
                    small_num += 1
                elif self.list_shape[i][j] == '+' and i > 0 and self.list_shape[i - 1][j] == '+' and left == '+' and \
                        self.list_shape[i - 1][j - 1] == '+':
                    self.small_vertices[small_num] = [i - 1, i, j - 1, j]
                    small_num += 1
                left = self.list_shape[i][j]
        return

    def cut_out_figure(self, num):
        coord = self.vertices[num]
        tmp = []
        for i in range(coord[0] - 1, coord[1] + 2):
            tmp.append(self.list_shape[i][coord[2] - 1:coord[3] + 2])

        depth = len(tmp) - 1
        width = len(tmp[0]) - 1
        for i in range(depth + 1):
            for j in range(width + 1):
                if tmp[i][j] not in ['-', '+', '|', num]:
                    tmp[i][j] = ' '
                elif tmp[i][j] == '-':
                    if (i > 0 and tmp[i - 1][j] == num) or (i < depth and tmp[i + 1][j] == num):
                        tmp[i][j] = '-'
                    else:
                        tmp[i][j] = ' '
                elif tmp[i][j] == '|':
                    if (j > 0 and tmp[i][j - 1] == num) or (j < width and tmp[i][j + 1] == num):
                        tmp[i][j] = '|'
                    else:
                        tmp[i][j] = ' '
                elif tmp[i][j] == '+':
                    touches_num = False
                    if i > 0 and j > 0:
                        touches_num = True if tmp[i - 1][j - 1] == num else touches_num
                    if i > 0 and j < width:
                        touches_num = True if tmp[i - 1][j + 1] == num else touches_num
                    if i < depth and j > 0:
                        touches_num = True if tmp[i + 1][j - 1] == num else touches_num
                    if i < depth and j < width:
                        touches_num = True if tmp[i + 1][j + 1] == num else touches_num

                    if i > 0:
                        touches_num = True if tmp[i - 1][j] == num else touches_num
                    if i < depth:
                        touches_num = True if tmp[i + 1][j] == num else touches_num
                    if j > 0:
                        touches_num = True if tmp[i][j - 1] == num else touches_num
                    if j < width:
                        touches_num = True if tmp[i][j + 1] == num else touches_num

                    if not touches_num:
                        tmp[i][j] = ' '
        for i in range(depth + 1):
            for j in range(width + 1):
                if tmp[i][j] == num:
                    tmp[i][j] = ' '
                elif tmp[i][j] == '+':

                    if i < depth and i > 0 and tmp[i + 1][j] in ['|', '+'] and tmp[i - 1][j] in ['|', '+']:
                        tmp[i][j] = '|'
                    elif j < width and j > 0 and tmp[i][j + 1] in ['-', '+'] and tmp[i][j - 1] in ['-', '+']:
                        tmp[i][j] = '-'

                    if i < depth and i > 0 and j < width and j > 0:
                        count = 0
                        if tmp[i + 1][j] in ['|', '+']:
                            count += 1
                        if tmp[i - 1][j] in ['|', '+']:
                            count += 1
                        if tmp[i][j + 1] in ['-', '+']:
                            count += 1
                        if tmp[i][j - 1] in ['-', '+']:
                            count += 1
                        if count >= 3:
                            tmp[i][j] = '+'

        result = "\n".join([("".join(x)).rstrip() for x in tmp])
        self.cut_figures.append(result)

    def cut_out_small(self, small_num):
        coord = self.small_vertices[small_num]
        tmp = []
        for i in range(coord[0], coord[1] + 1):
            tmp.append(self.list_shape[i][coord[2]:coord[3] + 1])

        depth = len(tmp) - 1
        width = len(tmp[0]) - 1
        for i in range(depth + 1):
            for j in range(width + 1):
                if tmp[i][j] == '/':
                    tmp[i][j] = '|'
                elif tmp[i][j] == '_':
                    tmp[i][j] = '-'
        result = "\n".join([("".join(x)).rstrip() for x in tmp])
        self.cut_figures.append(result)

    def make_figures_list(self):
        for i in range(self.depth):
            for j in range(self.width):
                if self.list_shape[i][j] == '/':
                    self.list_shape[i][j] = '|'
                elif self.list_shape[i][j] == '_':
                    self.list_shape[i][j] = '-'
        for y in self.small_vertices:
            self.cut_out_small(y)
        for y in self.vertices:
            if y not in self.fake_vertices:
                self.cut_out_figure(y)
                # print("+++++++++++++++")
                # print(y, ": ", self.vertices[y])
        return

    def print(self):
        for x in self.list_shape:
            print(x, self.width)
        print("____")
        for y in self.vertices:
            if y not in self.fake_vertices:
                print(y, ": ", self.vertices[y])


def break_evil_pieces(shape):
    # shape = shape.replace(" ", "0")
    s = shape.splitlines()

    result = Solution(shape)
    result.overview_traversal()
    # result.print()
    result.make_figures_list()

    return result.cut_figures


def my_first_interpreter(code):
    val = 0
    result = []
    for c in code:
        if c == '+':
            val = 0 if val == 255 else val + 1
        elif c == '.':
            result.append(chr(val))
    return "".join(result)


def interpreter_smallfuck(code, string_tape):
    print("code: ", code)
    print("tape: ", string_tape)
    flip = {
        '0': '1',
        '1': '0'
    }
    tape = [*string_tape]
    cell = 0
    length_tape = len(tape)
    i = 0
    length_code = len(code)
    while i < length_code:
        if code[i] == '*':
            tape[cell] = flip[tape[cell]]
        elif code[i] == '<':
            if cell > 0:
                cell -= 1
            else:
                return "".join(tape)
        elif code[i] == '>':
            if cell < length_tape - 1:
                cell += 1
            else:
                return "".join(tape)
        elif code[i] == '[' and tape[cell] == '0':
            stack = 0
            while i < length_code:
                if code[i] == ']':
                    stack -= 1
                elif code[i] == '[':
                    stack += 1
                if stack == 0:
                    break
                i += 1
            if i == length_code:
                i -= 1
        elif code[i] == ']':
            stack = 0
            while i >= 0 and stack != 0:
                if code[i] == ']':
                    stack -= 1
                elif code[i] == '[':
                    stack += 1
                if stack == 0:
                    break
                i -= 1
            if i < 0:
                i += 1
        i += 1
    return "".join(tape)

print(interpreter_smallfuck("*>[[]*>]<*", "100"))







