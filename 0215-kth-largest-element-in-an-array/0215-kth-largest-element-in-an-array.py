class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #1,2,3,4,5,6

        #1,2,2,3,3,4,5,5,6
        nums.sort()
        

        return nums[len(nums)-k]