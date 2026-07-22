class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1
        first = float('inf')
        while left <= right:
            mid = (left+right)//2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:#nums[mid] <= nums[right]
                if nums[mid] < first:
                    first = nums[mid]
                right = mid - 1 
        
        return first
        
"""       

[3,1,2]
 l 
 r
 m


    if the smallest value is at index 0, then that means the array is sorted and not rotated, arr[mid] <= arr[right] always

    if rotated, arr[mid] > arr[right] so we need to look at the right side for the smallest/first number

    If the mid candidate is valid, if num[mid] < num[righ]--that doesnot guarentee that the mid element is the lowest value so we will further look on the left side to get a potentially lower element



    nums[mid] > nums[r]: left=mid+1 --that means it was rotated and the lowest element is in the right side, if the smalles element is in the index 0, it means it was fully sorted, this condition would never happen and that nums[mid]<nums[right]

    nums[mid] <= nums[right]: right=mid-1 --that means we did find a potential candidate but to get the lowest element we need to look for less values on the left side, since nums[mid] <= nums[right] the array is sorted and we only need to look on the left to get lower values

    when exiting the loop, return nums[left]

"""


  