import Queue, random

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    q = Queue.PriorityQueue()
    for x in nums:
        q.put(x)
        if(q.qsize() > k):
            q.get()

    return q.get()

random_nums = [random.randint(0,50) for _ in xrange(8)]
print random_nums
print findKthLargest(random_nums, 4)