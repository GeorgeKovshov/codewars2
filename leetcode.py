def reverseWords(s):
    #exp = s.split()
    #str = " ".join([x for x in s.split()[::-1]])
    #for x in exp:
    #    print(x)
    #print(str)
    return " ".join([x for x in s.split()[::-1]])

#print(reverseWords("small dog meets a cat"))

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
:type head: ListNode
:rtype: bool
"""
def hasCycle(head):
    slow = head
    fast = head
    while fast and slow:
        try:
            slow = slow.next
            fast = fast.next.next
        except:
            return False
        if fast == slow:
            return True
    return False


def tryingClasses(head):
    tmp1 = head
    slow = head
    fast = head
    while head:
        print(head.val)
        head.val = head.val + 1

        head = head.next
    while tmp1:
        print(tmp1.val)
        tmp1 = tmp1.next
    return


tmp = ListNode(2)
tmp.next = ListNode(3)
tmp.next.next = ListNode(4)

tryingClasses(tmp)

"""
while tmp:
    print(tmp.val)
    tmp = tmp.next
"""
