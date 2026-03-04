class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        #nums = [-3,2,-3, 4,2]
        #pref = [-3,-1,-4,0,2] 
        #minVal = 5
        #pref = 2
        startVal = pref = 1
        for n in nums:
            pref += n
            while pref < 1:
                startVal += 1
                pref += 1 
        return startVal
