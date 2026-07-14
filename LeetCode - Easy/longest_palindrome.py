class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hm = {}
        for v in s:
            hm[v] = hm.get(v, 0) + 1
            
        rest = False
        t = 0
        for v in hm:
            if hm[v] % 2 == 0:
                t += hm[v]
            else:
                t += hm[v] - 1
                rest = True
                
        if rest:
            t += 1
        return t