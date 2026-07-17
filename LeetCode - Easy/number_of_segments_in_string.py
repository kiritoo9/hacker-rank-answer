class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        return len([v for v in s.split(" ") if v != "" and v != " "])