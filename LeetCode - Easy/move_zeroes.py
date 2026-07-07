class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        z = 0
        while (i+z) < len(nums):
            if nums[i] == 0:
                val = nums[i]
                nums.pop(i)
                nums.append(val)
                z += 1
            else:
                i +=1

        return nums
