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


