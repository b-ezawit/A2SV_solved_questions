class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            total_days = 1
            current_weight = 0
            for weight in weights:
                if current_weight + weight > capacity:
                    total_days += 1
                    current_weight = weight
                else:
                    current_weight += weight
            
            return total_days <= days
        
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low+high)//2
            if can_ship(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
        









""" 
       for every mid_weight, can_ship is computed, which is a function that assumes mid_weight as the capacity/total-weight that can be shipped per day, and it iterates over all the given weights and it checks whether the-sum-of-the-previous-weights + the_current_weight is <= capacity/mid_weight, if it is, it keeps on adding that weight and checks the next weights, if it is not then it increments the number of days to ship as  the-sum-of-the-previous-weights + the_current_weight is > capacity, the-sum-of-the-previous-weights will be shipped in one day and within a new day, the current_weight will be shipped. So this function simply takes the mid_weight as the capacity-per-day and it counts all the total-days it takes to finish shipping all the weights making the capacity per-day to be the mid_weight, and if the total days to finish shipping all the weights exceeds using this capacity > D-days, it return False. If the total_days <= D-days it returns true, so we keep on searching for the lowest posiible total-weight/capacity that can be shipped per-day so that all the given elements in weights arr can be shipped within D-days

        low = min amount of weight i can ship per day == max(weight) == is a single weight and this single weight must not be less value, i i ship only one item per day then that must be the maximum value of the whole array

        high = max amount of weight i ship per day is all they items, sum(weights) within one day, the maximum possible weight i can ship per day.

        the question asks the minimum amount of weight to ship so that with in D days, all of the weights are shipped

        low=max(weights)    mid_weight   high=sum(weights)
        So i must search on the left side as much as possible so that i can get the lowest possible total-weight that can be shipped per day only so that within the D-days, in days <= D  all the weights need to be shipped.

        so:
        condition 1:
            the mid_weight is valid, can_ship(mid_Weight) is true, that means if we pick the mid_weight to be the capacity/amount of the allowed weight that can be shipped then within <= D days all the weights can be shipped, so taking mid_weight as a capacity per day is valid. But if the mid_weight taken as a per-day capacity does not neccessarily mean that this mid_weight is the least possible weight that can be shipped per day with in <= D days. There may be a lower weight that mid_weight that can still be valid, that we can consider as a capacity per-day in such a way that all the weights can be shipped successfully within <= D days, so we must track the mid_weight as a valid candidate and still look for more on the left side if we could potentially get a much lower weight and use it as a capacity per day that will make all the weights shipped within <= D days.
            to search in the left side for lower capacity/total-weight per day that could successfully ship all the weights within <= D days, make: high = mid - 1 

        condition 2:
            the mid_weight is invalid, can_ship(mid_weight) is false, the means if we choose the mid_weight to be the capacity/amount of total-weight to be shipped per day, then we won't be able to ship/finish shipping all the given weights within <= D says, infact, it means that we made the daily capacity(mid_weight) too low that the total number of days to finish shipping all the given weights using this capacity per-day has resulted in total-days of shipping to be > D days, so it means the amount of capacity per-day is to small so everyday we get to ship either one or small number of the given days resulting in needing more days > D days to finish shipping. So we must increment the amount of capacity / total-weight per day so that more number of weights can bw shipped per-day in such a way that we finish shipping quicker in <= D days. So we must look for higher weights.
            In other words, the mid_weight is invalid because the function cna_ship resulted in total_days > D-days
            which means that the mid_weight/capacity per day is too low to finish shipping earlier in  <= D-days and that per day since we are taking very small amount of weights to ship, it took us more days that D-days, we couldn't finish sooner. So we need to have a greater weight as a capacity that could make us ship more number of weights per day so that we can finish shipping quicker in <= D-day.
            So to search for larger elements in the right: low = mid + 1



        
        in binary search, if we're looking for the smallest possible element/first element, even if the mid is a valid candidate, we will still look at the left side, high=mid-1 to get a lower working value and at last we return low.

        if we're looking for the largers possible element/last element, even if the mid candidate is valid, we'll still look in the right side to get a larger element, low=mid+1. we return high.

        we don't neet to blindly do binary search on any given array, for example in this problem the array is not sorted, and we need to calculate the total number of days it takes us to ship the weights sequentially, so we cannot sort it, so we must think of other value where we can compute binary search on
        Since binary search must be used on sorted values, searching in a sorted weight, which starts from max(array) to sum(array) --since elements are positive the sums is always greater.

        eg: weights = [3,2,2,4,1,4] we didnot blindly apply binary search on the array
        binary search done on:

        max(weights) till sum(weights)
        4              10          16
        low           mid         high


the hint says:
Binary search on the answer. We need a function possible(capacity) which returns true if and only if we can do the task in D days.


Binary search on the answer. --means on the capacity or total_weight per day
                            -> the lowest possible total_weight per day that can result in shipping all the weights in <= D-days
                    -> so we need to search on the answer / capacity per-day
                    
                    from the lowest possible weight to be shipped per-day==max(weights)
                                        |
                                        |
                                        | to
                                        |
                                        |
                   the hights posiible weight to be shipped per-day==sum(weights)



                   and with in this range, to get the lowest possible weight that works(ships all the weights within <= D-days)

"""        



        