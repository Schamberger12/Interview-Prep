"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Solution outline:
            #Create a set from the input array nums
            #Loop through the input array nums.
            # Check if the the current number is the beginning of a sequence
            # by checking if there's a number previous to it,
            # if there is, run through the sequence and save the count of that sequence. 
        num_set = set(nums)
        count = 0
        curr_len = 0

        for num in nums:
            # Check if the number is the start of a sequence
            # If it is, keep checking if the next number exists in the sequence
            if (num - 1) not in num_set:
                curr_len = 0
                while (num + curr_len) in num_set:
                    curr_len += 1
                if curr_len > count:
                    count = curr_len
        return count
                



