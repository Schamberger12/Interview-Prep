"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # First thought is to do 2 sum array is sorted. 
        nums.sort()

        # Fix the first number in place, and then have a middle and end variable 

        num_list = []

        sum = 0

        for i in range(len(nums)):
            # Don't want duplicates, shift right if i == i + 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # need to reset 2sum pointers every iteration
            # Otherwise, the right pointer will miss certain sums. 
            l = i+1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    num_list.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # shift l to the right if there's a duplicate
                    # also need to make sure l < r
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return num_list
                
        





