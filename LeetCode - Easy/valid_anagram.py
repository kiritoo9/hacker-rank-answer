class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        def extract(val):
            hm = {}
            for v in list(val):
                if v in hm:
                    hm[v] += 1
                else:
                    hm[v] = 1
                    
            return hm

        return extract(s) == extract(t)