class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        sortedN = sorted(nums)
        for i in range(len(sortedN)):
            curr_elem = sortedN[i]
            left = i+1
            right = len(sortedN)-1
            
            target = 0-curr_elem

            while left<right:
                if sortedN[left]+sortedN[right]==target:
                    res.append([curr_elem,sortedN[left],sortedN[right]])
                    left += 1
                    right -= 1
                elif sortedN[left]+sortedN[right]<target:
                    left += 1
                else:
                    right -= 1
        ans = []
        
        for t in res:
            if t in ans:
                continue
            else:
                ans.append(t)
        return ans


        