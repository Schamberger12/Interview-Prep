"""
875. Koko Eating Bananas
Solved
Medium
Topics
Companies
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        """
        
        Use binary search to attempt each number in the range 1..largest where largest is the largest number in piles. 

        Using binary search, Get the sum of how long to eat each pile of bananas using a given number from the range 1..largest 
	        eg. k = [1..11], piles = [3, 6, 7, 11], h = 8
	        Try using 6 on each pile:
		        3/6 = 1 | 6/6 = 1| 7/6 = 2 | 11/6 = 2
		        1 + 1 + 2 + 2 = 6 
	        Is 6 greater or less than 8?
		    Less than, so iterate binary search by setting l = m + 1
        """

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            pile_sum = 0
            for num in piles:
                pile_sum += math.ceil(float(num) / m)
            
            if pile_sum <= h: 
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res
        



