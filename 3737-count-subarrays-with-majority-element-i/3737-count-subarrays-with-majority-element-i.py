class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:

        '''
        target=3
        nums = [2,4,3,3,3,3]
        countTarget = nums.count(3) = 4

        half = len(subArr) // 2

        countTarget > half

        countTarget > len(subArr)//2

        if countTarget * 2 > len(subArr)
            res += 1


        '''
        nums_count = Counter(nums)
        ans = 0
        sub_arr = []
        count = 0

        l,r = 0,0
        while l<len(nums):            
            if r >= len(nums):
                l += 1
                r = l
                if l < len(nums):
                    sub_arr = []
                    count = 0
                continue
            
            sub_arr.append(nums[r])
            if nums[r] == target:
                count +=  1

            if 2 * count > len(sub_arr):
                ans += 1
            r += 1
        
        return ans



            
