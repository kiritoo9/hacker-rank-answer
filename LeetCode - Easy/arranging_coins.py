class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        while n > 0:
            c = i+1
            if n < c:
                break
            
            n -= c
            i += 1
            
        return i