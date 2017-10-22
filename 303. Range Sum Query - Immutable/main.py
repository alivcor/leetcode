class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.hashmap = {}
        self.precomputeN()

    def precomputeN():
        for x in range(len(nums)):
            if x == 0:
                self.hashmap[x] = self.nums[x]
            else:
                self.hashmap[x] = self.hashmap[x - 1] + self.nums[x]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.hashmap(j) - self.hashmap(i)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)