"""
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Very similar to two Sum, but using area instead of sum

        # Create two pointers, left and right. 
        # Every iteration, get the area by multiplying the lower height
        # by the difference between the heights
        # If the left height is lower, increment left
        # If the right height is lower, decrement right. 

        l = 0
        r = len(height) - 1
        area = 0
        largest_area = 0

        while l != r:
            # Get the area 
            if height[l] > height[r]:
                area = height[r] * (r-l)
                r -= 1
            else:
                area = height[l] * (r-l)
                l += 1
            
            if area > largest_area:
                largest_area = area

        return largest_area
