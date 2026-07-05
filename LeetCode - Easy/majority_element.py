class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}
        for n in nums:
            if n in dp:
                dp[n] += 1
            else:
                dp[n] = 1

        return max(dp, key=dp.get)
        