class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        approach:
        (sum[right] - sum[left-1]) % k = 0
        sum[right]%k - sum[left-1]%k = 0 

        1. sum[right]%k = sum[left-1]%k --remainder needs to be the same
        2. lenght >= 2

        hmap{remainder:index}

        check if curr_remainder is in hmap and lenght >=2
        '''
        _sum = 0
        hmap = {0 : -1}
        for i in range(len(nums)):
            _sum += nums[i]
            remainder = _sum % k
            if remainder in hmap:
                if i - hmap[remainder] >= 2:
                    return True
            else:
                hmap[remainder] = i
        return False

            
            


        