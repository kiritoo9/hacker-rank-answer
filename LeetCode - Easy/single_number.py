class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hm = {}
        for n in nums:
            if n not in hm:
                hm[n] = None
            else:
                del hm[n]

        if len(hm) <= 0:
            return 0
        else:
            k,_ = next(iter(hm.items()))
            return k
        