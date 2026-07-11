class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = ["a","i","u","e","o"]
        dp = []
        for i, v in enumerate(s):
            if v.lower() in vowels:
                dp.append([v, i])
        
        dps = list(s)
        for i in range((len(dp)-1), -1, -1):
            dps[dp[(len(dp)-1)-i][1]] = dp[i][0]
            
        return "".join(v for v in dps)
        