
"""

    Problem condition in leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

"""

class Solution(object):
    def removeDuplicates(self, nums):
        count = 1
        index = 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[index]:
                nums[index+1],nums[i] = nums[i],nums[index+1]
                index+=1
                count+=1


        return count