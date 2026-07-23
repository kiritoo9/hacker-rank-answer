class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        i = 0
        ans = 0
        while i < len(s):
            sub = set()
            j = i
            
            while j < len(s) and s[j] not in sub:
                sub.add(s[j])
                j += 1

            ans = max(ans, len(sub))
            i += 1
                
        return ans