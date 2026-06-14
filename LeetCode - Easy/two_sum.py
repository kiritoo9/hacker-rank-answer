class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        storage = {}
        for i, n in enumerate(nums):
            m = target-n
            if m not in storage:
                storage[n] = i
            else:
                return [i, storage.get(m)]