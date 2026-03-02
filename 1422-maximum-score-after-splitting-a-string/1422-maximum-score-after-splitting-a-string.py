class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        right = s.count('1')
        max_score = 0 
        left = 0
        
        for i in range(len(s)-1):
            c = s[i]
            if c=='0':
                left += 1
            else:
                right -= 1
            max_score = max(max_score, left+right)
        
        return max_score
        