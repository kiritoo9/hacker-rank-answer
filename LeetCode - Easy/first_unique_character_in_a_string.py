class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hm = {}
        for v in s:
            hm[v] = hm.get(v, 0) + 1
        
        for i, v in enumerate(s):
            if hm[v] == 1:
                return i
        
        return -1