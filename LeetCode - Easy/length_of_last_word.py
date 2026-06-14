class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        spl = [v for v in s.split(" ") if v != ""]
        return len(spl[-1])