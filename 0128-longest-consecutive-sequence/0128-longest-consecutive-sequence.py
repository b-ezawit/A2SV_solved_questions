class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ''' Bruteforce:
        if len(nums)==0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        maxCon = 0
        temp = 0
        left = 0
        right = 1
        #[1,1,2,3,4,5,5] temp = 0
        while right < len(nums):
            if nums[right] - nums[left] == 1:
                temp += 1
            elif nums[right] - nums[left] > 1:
                temp = 0
            left += 1
            right += 1
            maxCon = max(maxCon , temp)
        return maxCon + 1
        '''

        setN = set(nums)
        maxCon = 0
        for n in setN:
            if n-1 not in setN:
                currCon = 1
                while n + currCon in setN:
                    currCon += 1
                maxCon = max(maxCon, currCon)
        
        return maxCon
