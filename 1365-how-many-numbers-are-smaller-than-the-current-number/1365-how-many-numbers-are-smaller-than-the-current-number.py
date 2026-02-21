class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
       
        nums_sort = sorted(nums)

        for i in range(len(nums)):
            count = 0
            indx_in_sort = nums_sort.index(nums[i]) #if nums[i] = 8, nums_in_sort.index(8) is 4 
            for j in range(indx_in_sort):
                if nums_sort[j] < nums[i]:
                    count += 1
            nums[i] = count
        
        return nums
            


        





        