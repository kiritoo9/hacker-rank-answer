class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def to_hm(input):
            hm = {}
            for i in input:
                hm[i] = hm.get(i, 0) + 1
            
            return hm
            
        hm_s = to_hm(s)
        hm_t = to_hm(t)
        diff = []
        
        for v in hm_t:
            if v not in hm_s:
                diff.append(v*hm_t[v])   
            else:
                c = abs(hm_t[v]-hm_s[v])
                if c > 0:
                    diff.append(v*c)
                
        return "".join(v for v in diff)