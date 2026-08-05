class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_indx(arr,target):
            left = 0
            right = len(arr)-1

            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > target or arr[mid] == target:
                    right = mid - 1
                else: 
                    left = mid + 1
            
            if left < len(arr) and arr[left] == target:
                return left 
            else:
                return -1        

        def last_indx(arr,target):
            left = 0
            right = len(arr)-1

            while left <= right:
                mid = (left + right) // 2

                if target > arr[mid] or target == arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            if right >= 0 and arr[right] == target:
                return right 
            else:
                return -1
        
        return [ first_indx(nums,target) , last_indx(nums,target) ]
    
        
       

            
            





                     





        



