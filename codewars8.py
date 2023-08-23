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