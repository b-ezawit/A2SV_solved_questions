class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s = "AABABBA", k = 1
        left = maj = maxlen = 0

        hmap = defaultdict(int)#stores valid substring with the count of each char

        for right in range(len(s)):
            hmap[s[right]] += 1#hmap = {'A':1}
            maj = max(maj,  hmap[s[right]])
            while maj + k < right - left + 1:
                hmap[s[left]] -= 1
                if hmap[s[left]]<=0:
                    del hmap[s[left]]
                left += 1
            maxlen = max(maxlen,right-left+1)
        return maxlen
