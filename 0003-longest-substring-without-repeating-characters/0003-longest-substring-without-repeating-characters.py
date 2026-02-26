class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Approach => left=0, r=0 hmap=> key=char v=count
        #iterate for each char, hmap[char]+=1 while hmap[char]>1: hmap[char]-=1 del if hmap[char]==0, left+=1, maxlen = max(r-l+1, maxlen)
        hset = set()
        maxlen = 0
        l,r = 0,0
        n = len(s)
        maxlen = 0
        while r<n:
            while s[r] in hset:
                hset.remove(s[l])
                l += 1
            hset.add(s[r])
            maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen