class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        idx = -1
        for i in range(0, len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                idx = i
                break
            
        return idx