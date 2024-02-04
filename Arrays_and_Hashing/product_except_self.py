class Solution(object):
"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

"""
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #loop through the input array twice
        #   once to get the product before the number
        #   twice to multiply the product before the number by the prodcut after the number
        #   EX: [1, 2, 3, 4]
        #       [1, 1, 2, 6]
        #       [24, 24, 12, 4]
        #       [24, 12, 8, 6]
        #       solution: position 2, multiply 1 * 12 to get 12
        #                 position 3, multiply 2 * 4 to get 8
        #                 position 4, multiply 6 * 1 to get 6


        
        result = [1] * (len(nums))
        product = 1

        for i in range(len(nums)):
            result[i] = product
            product *= nums[i]

        product = 1
        print(result)
        for j in range(len(nums) - 1, -1, -1):
            result[j] *= product
            product *= nums[j]
        
        return result
    

