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

print(cut_the_ropes([3, 3, 2, 9, 7]))
print(cut_the_ropes([1, 2, 3, 4, 3, 3, 2, 1]))


def freed_prisoners(prison):
    current = True
    count = -1
    for p in prison:
        if p == current:
            current = not current
            count += 1
    return count

















