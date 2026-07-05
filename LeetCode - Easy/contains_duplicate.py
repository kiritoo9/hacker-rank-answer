class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = set()
        for n in nums:
            if n in dp:
                return True
            else:
                dp.add(n)
        return False