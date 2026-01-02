class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ones = 0
        zeros = 0
        twos = 0
        for n in nums:
            if n==0:
                zeros+=1
            elif n==1:
                ones += 1
            else:
                twos += 1
        
        for i in range(zeros):
            if zeros>0:
                nums[i] = 0
        
        for j in range(zeros,zeros+ones):
            if ones>0:
                nums[j] = 1
        
        for k in range(zeros+ones,zeros+ones+twos):
            if twos>0:
                nums[k] = 2
        
        return nums

        