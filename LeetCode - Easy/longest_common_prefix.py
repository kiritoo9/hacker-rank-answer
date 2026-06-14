class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs[0] == "":
            return ""


        idx_string = 1
        check_string = strs[0][0:idx_string] # starter string
        longest_string = ""
        while True:
            not_same = False

            for s in strs:
                if check_string != s[0:idx_string]:
                    not_same = True
                    break


            if not_same:
                break
            else:
                longest_string = check_string

                # increasing index
                idx_string += 1
                if idx_string <= len(strs[0]):
                    check_string += strs[0][idx_string-1]
                else:
                    break

        return longest_string


        