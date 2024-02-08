class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Create a sliding window in which we start with the
        # whole array and whittle down the sides. 
        
        # Check the value of the smallest number
        # and sum that with the largest number, 
        # continuously remove the largest number until 
        # the sum is found, or the sum is smaller than the target. 

        # Once the sum is smaller than the target,
        # remove the smallest number

        # Setup the window pointers
        l = 0
        r = len(numbers) - 1
        total = numbers[l] + numbers[r]

        while True:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -=1
            elif numbers[l] + numbers[r] < target:
                l +=1



        
		
	
        