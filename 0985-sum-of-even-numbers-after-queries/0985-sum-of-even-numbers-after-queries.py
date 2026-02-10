class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        '''
        result = []

        for val,indx in queries:
            nums[indx] += val
            sum_even = 0
            for num in nums:
                if num % 2 == 0:
                     sum_even += num
            result.append(sum_even)
        
        return result
        '''

        result = []
        sum_even = 0
        for num in nums:
            if num % 2 == 0:
                sum_even += num

        for val,indx in queries:
            if (nums[indx] + val) % 2 == 0:
                sum_even += (nums[indx] + val)
            
            if nums[indx] % 2 == 0:
                sum_even -= nums[indx]

            nums[indx] = nums[indx] + val
            result.append(sum_even)
        
        return result








