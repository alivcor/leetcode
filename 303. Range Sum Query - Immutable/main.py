class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < j:
            return self.nums[i] + self.nums[j] + self.sumRange(i + 1, j - 1)
        elif i == j:
            return self.nums[i]
        else:
            return 0

