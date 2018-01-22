# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def appendNode(self, val):
        x = self
        while(x.next):
            x = x.next
        x.next = ListNode(val)

    def appendList(self, list):
        for val in list:
            self.appendNode(val)

    def printList(self):
        x = self
        while (x):
            print x.val, "-->",
            x = x.next
        print None

def mergeTwoListsIteratively(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    prehead = ListNode(-1)
    pointer = prehead
    while l1 and l2:
        if l1.val <= l2.val:
            pointer.next = l1
            l1 = l1.next
        else:
            pointer.next = l2
            l2 = l2.next
        pointer = pointer.next
    pointer.next = l1 if l1 is not None else l2
    return prehead.next

def mergeTwoListsRecursively(l1, l2):
    if(l1 is None):
        return l2
    elif l2 is None:
        return l1
    elif l1.val <= l2.val:
        l1.next = mergeTwoListsRecursively(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoListsRecursively(l1, l2.next)
        return l2

def initLists():
    l1 = ListNode(10)
    l1.appendList([20, 30, 40, 50, 60])
    l1.printList()
    l2 = ListNode(9)
    l2.appendList([21, 34, 35, 42, 50])
    l2.printList()
    return l1, l2

l1, l2 = initLists()
l3 = mergeTwoListsIteratively(l1, l2)
l3.printList()

l1, l2 = initLists()
l3 = mergeTwoListsRecursively(l1, l2)
l3.printList()