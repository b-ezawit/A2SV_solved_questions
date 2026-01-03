class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        ans = []
        total = sum(nums)
        nums.sort()
        r = len(nums)-1
        sublen = len(nums)
        for n in queries:
            temp = total
            templen = sublen
            while n<total and r>=0 and sublen>=0:
                total -= nums[r]
                sublen -= 1
                r -= 1
            ans.append(sublen)
          
            total = temp
            sublen = templen
            r = len(nums)-1
        
        return ans
    




