class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        l_to_r = []
        for i in range(left,right+1):
            l_to_r.append(i)

        elementsInRanges = []
        for r in ranges:
            for n in range(r[0],r[1]+1):
                elementsInRanges.append(n)
        #all elements in ranges= [1,2,3,4,5,6]
        
        for i in range(len(l_to_r)):
            if l_to_r[i] not in elementsInRanges:
                return False
        
        return True
