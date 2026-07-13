class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        def toHashMap(s):
            hm = {}
            for v in list(s):
                hm[v] = hm.get(v, 0) + 1
                
            return hm
        
        hm1 = toHashMap(ransomNote)
        hm2 = toHashMap(magazine)
        
        for key in hm1:
            if key not in hm2 or hm2[key] < hm1[key]:
                return False
        return True