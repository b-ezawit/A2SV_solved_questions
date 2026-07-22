class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_finish_in_h_hrs(banana_per_hr):
            total_hrs = 0
            for bananas in piles:
                if bananas <= banana_per_hr:
                    total_hrs += 1
                else:
                    total_hrs += math.ceil(bananas / banana_per_hr)
            return total_hrs <= h
        
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low+high) // 2
            if can_finish_in_h_hrs(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low

"""
ith pile = number of bananas in pile[i]

koko decides bananas per hour == k

koko chooses one pile and eats k bananas from it

if the pile[i] <= k: koko eats all of the pile

else if pile[i] > k: koko eats k and pile[i] - k will be left

return: min val k, so that koko eats all the bananas within h hours


"""
