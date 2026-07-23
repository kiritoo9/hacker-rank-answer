'''
Method: Expand Around Center
Core Idea: Find the center of string
Issue: Even string have no center, so it have different logic
Solution:
    - Odd = left, right
    - Even = left, right+1
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        left, right = 0, 0
        for i in range(len(s)):
            lood, rood = expand(i, i)
            leven, reven = expand(i, i+1)
            
            if rood-lood > left-right:
                right, left = lood, rood
                
            if reven-leven > left-right:
                right, left = leven, reven
                
        return s[right:left+1]