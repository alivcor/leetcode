import random

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # print nums
    len_nums = len(nums)
    output = [1]*len_nums
    output[0] = 1
    for x in xrange(1, len_nums):
        output[x] = output[x-1]*nums[x-1] #ll[1] = ll[0]*nums[0]
    p = 1
    for x in xrange(len_nums-1, -1, -1):
        output[x] = output[x]*p
        p = p*nums[x]
    return output


def productExceptSelfA(nums):
    p = 1
    n = len(nums)
    output = []
    for i in range(0, n):
        output.append(p)
        p = p * nums[i]
    # print output
    p = 1
    for i in range(n - 1, -1, -1):
        output[i] = output[i] * p
        p = p * nums[i]
    return output

def generateList():
    return [random.randint(1, 30) for x in xrange(4)]

rlist = generateList()
print rlist
print productExceptSelf(rlist)
print productExceptSelfA(rlist)