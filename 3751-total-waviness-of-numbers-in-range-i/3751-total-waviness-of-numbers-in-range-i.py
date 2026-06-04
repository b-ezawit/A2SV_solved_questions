class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        nums = [num for num in range(num1,num2+1)]
        nums = list(map(str,nums))
        ans = 0
        for num in nums:
            for i in range(1, len(num)-1):
                if num[i-1]<num[i] and num[i]>num[i+1] or num[i-1]>num[i] and num[i]<num[i+1]:
                    ans += 1
        
        return ans
