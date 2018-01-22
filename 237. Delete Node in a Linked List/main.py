# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next



l = ListNode(10)
l.next = ListNode(5)
l.next.next = ListNode(2)
x = l
while(x):
    print x.val, "-->",
    x = x.next

print "None"

l.deleteNode(l.next)

x = l
while(x):
    print x.val, "-->",
    x = x.next