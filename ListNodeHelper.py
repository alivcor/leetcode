class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)
    
def getListNode(plist):
    dummy = ListNode(-1)
    curr = dummy
    for i in plist:
        curr.next = ListNode(i)
        curr = curr.next
    return dummy.next