class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        sCount = Counter(s)
        tCount = Counter(t)

        res = 0        
        for val,freq in sCount.items():
            if freq > tCount[val]:
                res += freq - tCount[val]
            
        
        return res
            
        
      


        return res
        
