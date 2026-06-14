class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        idx = 0
        for i,n in enumerate(nums):
            if n == target:
                idx = i
                break
            elif target >= n:
                if (i+1) >= len(nums):
                    idx = len(nums)
                    break
                elif target < nums[i+1]:
                    idx = i+1
                    break

        return idx
