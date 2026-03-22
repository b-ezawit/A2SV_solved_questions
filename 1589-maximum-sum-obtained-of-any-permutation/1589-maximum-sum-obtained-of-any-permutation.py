class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        diff = [0] * n
        
        for start, end in requests:
            diff[start] += 1
            if end < n - 1:
                diff[end + 1] -= 1

        res = 0
        prefix = []
        current_sum = 0
        
        for i in range(len(diff)):
            current_sum += diff[i]
            prefix.append(current_sum)
        
        prefix.sort()
        nums.sort()
        
        for i in range(len(prefix)):
            value = prefix[i]  
            num = nums[i]
            res += value * num
        
        return res % (10 ** 9 + 7)