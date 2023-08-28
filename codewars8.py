def compare(a, b):
    if not a and not b:
        return True
    elif a and not b:
        return False
    elif not a and b:
        return False
    if a.val != b.val:
        return False
    left = compare(a.left, b.left)
    right = compare(a.right, b.right)
    if not left or not right:
        return False
    return True

def compare2(a, b):
    return a.val == b.val and compare2(a.left, b.left) and compare2(a.right, b.right) if a and b else a == b

def compare3(a, b):
  if a is None or b is None:
    return a is b
  return a.val == b.val and compare3(a.left, b.left) and compare3(a.right, b.right)

from collections import deque




def tree_by_levels(node):
    q = deque()
    q.append(node)
    result = []
    while q:
        tmp = q.popleft()
        if not tmp:
            return result
        if tmp.left:
            q.append(tmp.left)
        if tmp.right:
            q.append(tmp.right)
        result.append(tmp.value)
    return result

def tree_by_levels2(node):
    p, q = [], [node]
    while q:
        v = q.pop(0)
        if v is not None:
            p.append(v.value)
            q += [v.left,v.right]
    return p if not node is None else []

class Tree:
    def __init__(self, x):
        self.left =  None
        self.right = None
        self.val = x

#class Leaf(Tree): ...

#class Branch(Tree):
#    left:  Tree
#    right: Tree

tree = Tree(2)
tree.left = Tree(3)
print(tree.left.val)

if not tree.right:
    print("No")

queue = []


""" generators below """
from types import GeneratorType


def cosine():
    c = 0
    while True:
        yield [1, 0, -1, -1, 0, 1][c]
        c = (c+1)%6


def count():
    c = 0
    while True:
        yield c
        c += 1


def delta_simple(values, n):
#for normal inputs
    if n == 0:
        return values
    result = []
    for i in range(1, len(values)):
        result.append(values[i] - values[i-1])
    return delta_simple(result, n-1)


def delta_gen(values):
    l = iter(values)
    x = next(l)
    while l:
        y = next(l)
        yield y - x
        x = y


def delta(values, n):
    """this function takes a list or generator and returns a generator in both cases"""
    if n <= 1:
        return delta_gen(values)
    return delta(delta_gen(values), n-1)




print("____________________")

g = delta(count(), 2)
l1 = delta([3, 3, -5, 77], 2)
print(isinstance(g, GeneratorType))

#g = delta([1, 0, -1, -1, 0, 1], 0)
#print(next(g))
#print(next(g))
#print(next(g))


print(next(l1))
print(next(l1))

"""this delta is for when you need return a list or a gen for a list and gen respectively """
def delta_list(values, n):
    #for lists
    if n == 0:
        return values
    result = []
    for i in range(1, len(values)):
        result.append(values[i] - values[i-1])
    return delta_list(result, n-1)

def delta_gen_helper(values):
    #for generators
    l = iter(values)
    x = next(l)
    while l:
        y = next(l)
        yield y - x
        x = y

def delta_gen1(values, n):
    #for generators
    if n <= 1:
        return delta_gen_helper(values)
    return delta(delta_gen_helper(values), n-1)

def delta(values, n):
    if isinstance(values, GeneratorType):
        return delta_gen1(values, n)
    else:
        return delta_list(values, n)


def delta1(iter_, n):
    iter_ = iter(iter_) if n == 1 else delta1(iter_, n-1)
    prev = next(iter_)
    for v in iter_:
        yield v - prev
        prev = v


from itertools import pairwise


def delta2(values: iter, n: int) -> iter:
    return delta((b - a for a, b in pairwise(values)), n - 1) if n > 0 else values


def delta3(values, n):
    if not n:
        yield from values
    else:
        it = delta(values, n-1)
        x = next(it)
        for y in it:
            yield y-x
            x = y


def delta4(values, n):
    if not n:
        yield from values
    else:
        it = delta(values, n-1)
        x = next(it)
        for y in it:
            yield y-x
            x = y
