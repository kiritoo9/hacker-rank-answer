class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(s) <= 0:
            return 0

        g = sorted(g)
        s = sorted(s)
        content = set()
        visited = set()
        i = 0
        j = 0
        
        while i < len(g):
            if s[j] >= g[i] and j not in visited:
                content.add(i)
                visited.add(j)
                i += 1
            
            j += 1
            if j >= len(s):
                break
            
        return len(content)