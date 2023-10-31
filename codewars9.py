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

