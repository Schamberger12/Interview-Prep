"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

class Solution(object):
    def twoSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Loop through the array nums and store each in a
        #hash table of key: value pair integer: position. 
        #If there's an integer equal to target - current number, 
        #return the position of both numbers. 
        num_dict = {}
        sub = 0

        for i in range(len(nums)):
            # target will always be the higher of the 2 numbers
            # since the prompt is expecting nums[i] + sub == target. 
            sub = target - nums[i]
            if sub in num_dict.keys():
                return [num_dict[sub], i]
            else:
                num_dict[nums[i]] = i
        return False
