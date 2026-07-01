class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(v.lower() for v in s if v.isalnum())
        return  s == s[::-1]
            