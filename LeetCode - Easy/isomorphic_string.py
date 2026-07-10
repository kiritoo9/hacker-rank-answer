class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
    
        dp_s = {}
        dp_t = {}
        for cs, ct in zip(s, t):
            if cs in dp_s:
                if dp_s[cs] != ct:
                    return False
            else:
                dp_s[cs] = ct
            
            if ct in dp_t:
                if dp_t[ct] != cs:
                    return False
            else:
                dp_t[ct] = cs
                
        return True