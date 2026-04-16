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


        # nums = [4,-3,-2,-7,8,2,-3,-1]

        '''
        ans = []
        for n in nums:#n=-3
            if nums[abs(n)-1] < 0:#nums[0] 
                ans.append(abs(n))
            else:
                nums[abs(n)-1] = -nums[abs(n)-1]
        return ans
        '''
        ans = []
        for i in range(len(nums)):
            while nums[i] != i+1:
                if nums[i] == nums[nums[i]-1]:
                    ans.append(nums[i])
                    break
                pos = nums[i]-1
                nums[i],nums[pos] = nums[pos],nums[i]
        
        l,r = 0,1
        while r<len(nums):
            if nums[l] == nums[r]:
                ans.append(nums[l])
            l += 1
            r += 1
        return list(set(ans))



