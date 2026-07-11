class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hm = {}
        for n in nums2:
            if n not in hm:
                hm[n] = 1
            else:
                hm[n] += 1
                
        ans = []
        for n in nums1:
            if n in hm and hm[n] > 0:
                hm[n] -= 1
                ans.append(n)
                continue
       
        return ans