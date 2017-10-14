def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxval = 0
    val = 1
    if len(nums) <= 1: return len(nums)
    for i in xrange(len(nums) - 1):
        if (nums[i] < nums[i + 1]):
            val = val + 1
        else:
            val = 1
        if val > maxval:
            maxval = val
        print i, val, maxval
    return maxval