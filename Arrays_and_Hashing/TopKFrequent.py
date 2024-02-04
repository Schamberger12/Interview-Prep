"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        #Create hash table of type (integer: count)
        #Loop through nums, add or increment the count for each element in nums
        num_dict = {}

        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        #Sort the dictionary by value
        #Use sorted method, the below translates to return a list of the values of the dictionary in descending order
        #sorted parameters:
        #   1st == thing being sorted, num_dict.items() gets us the whole key: value pair
        #   2nd == lambda function to sort the dictionary entries by the values, aka sort by num_dict[1](values) not num_dict[0](keys)
        #   3rd == Descending order to make our lives easier
        sorted_dict = sorted(num_dict.items(), key=lambda x:x[1], reverse=True)

        return_list = []
        #Loop through the sorted values k times and append each to the result list
        for i in range(0, k):
            #Append
            return_list.append(sorted_dict[i][0])
        return(return_list)


        
        

        
        
