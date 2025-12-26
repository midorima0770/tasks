
"""

    Problem condition in leetcode: https://leetcode.com/problems/remove-element/

"""

class Solution(object):
    def removeElement(self, nums, val):
        result_list = []
        for i in range(len(nums)):
            if nums[i]!=val:
                result_list.append(nums[i])
        for i in range(1,len(result_list)):
            if nums[i-1] > nums[i]:
                nums[i-1],nums[i]= nums[i],nums[i-1]
        for i in range(len(result_list)):
            nums[i]=result_list[i]
        return len(result_list)