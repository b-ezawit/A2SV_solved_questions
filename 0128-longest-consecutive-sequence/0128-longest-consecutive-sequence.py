class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setN = set(nums)
        maxlen = 0
        for n in setN:
            
            if n-1 not in setN:
                length = 1
                while n+length in setN:
                    length += 1
                
                maxlen = max(length,maxlen)

        return maxlen

