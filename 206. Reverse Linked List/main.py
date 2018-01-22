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

    def reverseListIteratively(self):
        prev = None
        curr = self
        while(curr):
            nexttemp = curr.next
            curr.next = prev
            prev = curr
            curr = nexttemp
        return prev

    def reverseListRecursively(self):
        if self == None or self.next == None: return self
        reversedright = self.next.reverseListRecursively()
        self.next.next = self
        self.next = None
        return reversedright

def initLists():
    l1 = ListNode(10)
    l1.appendList([20, 30, 40, 50, 60])
    l1.printList()
    return l1

l1 = initLists()
l1 = l1.reverseListRecursively()
l1.printList()