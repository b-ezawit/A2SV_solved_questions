class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #brute force:
        #numsCount = Counter(nums)
        #return [k for k in numsCount if numsCount[k]==2]

        #elements in nums in range: [1,n]
        #nums = [4,3,2,7,8,2,3,1]
        #n=8, possible values=[1,2,3,4,5,6,7,8] 
        #              index:  0 1 2 3 4 5 6 7
        ans = []
        for n in nums:
            if nums[abs(n)-1] < 0:
                ans.append(abs(n))
            else:
                nums[abs(n)-1] = -nums[abs(n)-1]
        return ans