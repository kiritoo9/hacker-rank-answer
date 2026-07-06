class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1 = sum(nums)
        s2 = sum([i for i in range(1, len(nums)+1)])
        return s2-s1
        