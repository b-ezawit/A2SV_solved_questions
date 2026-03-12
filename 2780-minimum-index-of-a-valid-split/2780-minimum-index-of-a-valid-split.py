class Solution:

    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        countLeft = defaultdict(int)
        countRight = Counter(nums)
        for i in range(len(nums)):
            countRight[nums[i]] -= 1
            countLeft[nums[i]] += 1
            if countRight[nums[i]] <= 0:
                del countRight[nums[i]]
            
            leftCount = countLeft[nums[i]]
            rightCount = countRight[nums[i]]
            if leftCount*2 > i+1  and rightCount*2 > n-i-1:
                return i
        return -1


            
        
        