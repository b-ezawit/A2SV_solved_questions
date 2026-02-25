class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        n = len(nums)
        target_freq = math.floor(n/3)
        return [key for key,val in nums_count.items() if val > target_freq]

        