class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hm = set(nums)
        missing = []
        for i in range(1, len(nums)+1):
            if i not in hm:
                missing.append(i)

        return missing