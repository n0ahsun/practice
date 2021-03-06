class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]: continue #skip duplicates
            l = i+1
            r = len(nums) - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp == 0:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: # skip duplicates
                        l += 1
                    while l < r and nums[r] == nums[r + 1]: 
                        r -= 1                   
                elif temp > 0:
                    r -= 1
                else:
                    l += 1
        return list(result)

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Note:
# The solution set must not contain duplicate triplets.

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]