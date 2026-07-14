class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
    
        sidx = list(s)
        tidx = list(t)
        indexes = []
        visited = set()
        
        for i in sidx:
            if i not in tidx:
                return False
            
            idx = [
                _idx for _idx, v in enumerate(tidx) 
                if v == i 
                and _idx not in visited
            ]
            if len(idx) <= 0:
                return False
            
            if len(indexes) <= 0:
                indexes.append(idx[0])
                visited.add(idx[0])
            else:
                __idx = idx[0]
                for _idx in idx:
                    if _idx > indexes[-1]:
                        __idx = _idx
                        break
                
                if __idx < indexes[-1]:
                    return False
                    
                indexes.append(__idx)
                visited.add(__idx)
                
        return True