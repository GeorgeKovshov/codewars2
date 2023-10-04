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
    arr = []
    permute = []
    result = []


    def __init__(self, num):
        self.length = 0
        while num >= 1:
            self.arr.append(num % 10)
            #self.permute.append(num % 10)
            num = num // 10
            self.length += 1


    def recursive_find1(self, avail_ar, permuted_ar, power):
        length_avail = len(avail_ar)
        if length_avail < 1:
            return
        length_permuted = len(permuted_ar)
        for i in range(length_avail):
            for j in range(length_permuted):
                num = avail_ar[i] + permuted_ar[j] * 10

                if num in self.permute or num / pow(10, power) < 1:
                    continue
                self.permute.append(num)
                if num % 3 == 0:
                    self.result.append(num)
                self.recursive_find1(avail_ar[:i] + avail_ar[i+1:], permuted_ar + [num], power + 1)

        return

    def recursive_start(self):
        self.recursive_find1(self.arr, [0,0,0], 0)



def find_mult_3(num):
    arr = Multip(num)
    print(arr.arr)
    #arr.find(3)
    arr.recursive_start()
    #arr.recursive_find1(arr.arr)
    print(len(arr.result), max(arr.result))
    #print(sorted(arr.result))




print(find_mult_3(6063))

#ar = [1, 2, 3, 4, 5, 6, 7, 8]
#num = 2
#print(ar + [num])
#i = len(ar)-1
#print(ar[:i] + ar[i+1:])














