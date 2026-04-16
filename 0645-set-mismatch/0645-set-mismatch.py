class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            while nums[i] != i+1:
                if nums[i] == nums[nums[i]-1]:
                    if len(ans)==0:
                        ans.append(nums[i])
                    break
                pos = nums[i]-1
                nums[i],nums[pos] = nums[pos],nums[i]
        print("1st sort: ", ans)
        
        l,r = 0,1
        while r<len(nums):
            if nums[l] == nums[r] and len(ans) == 0:
                ans.append(nums[l])
            l += 1
            r += 1
        

        check = 1
        for i in range(len(nums)-1):
            num = nums[i]
            if num != check:
                ans.append(check)
                break
            if nums[i] != nums[i+1]:
                check = nums[i]+1

        if len(ans) == 1:
            if check == nums[-1]:
                ans.append(len(nums))
            else:
                ans.append(check)

        return ans        
        