class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #Approach: range= prefsum[right] - n*k = prefsum[left-1] 

        #rangesum = prefsum[left-1])= prefsum[right] - n*k
        #hmap={} key=prefsum val=count , 
        #for right in range(len(nums)): prefsum += nums[right]: if p
                            
        #time = O(n^2), space=O(n)
        hmap = {0:-1}
        prefsum = 0
        for r in range(len(nums)):
            prefsum += nums[r]
            rem = prefsum % k

            if rem in hmap:
                if (r-hmap[rem]) >= 2:
                    return True
            else:
                hmap[rem] = r
        return False

    
