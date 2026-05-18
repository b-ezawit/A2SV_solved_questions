class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low,high = 0,n-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid -1
            else:
                return mid
        
        if target > nums[mid]:
            return mid +  1
        
        else:
            return mid
        
