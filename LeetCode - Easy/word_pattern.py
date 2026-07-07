class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        p = list(pattern)
        a = s.split(" ")
        
        if len(p) != len(a):
            return False
        
        dp = {}
        took = set()
        status = True
        for i,v in enumerate(p):
            if v not in dp:
                if a[i] not in took:
                    took.add(a[i])
                    dp[v] = a[i]
                else:
                    status = False
                    break
            else:
                if a[i] != dp[v]:
                    status = False
                    break
                
        return status
        