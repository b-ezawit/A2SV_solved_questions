class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_map = {char : 0  for char in order}
        #{k:0, q:0, e:0, p:0} ---keeps each character in order
        for char in s:
            if char in char_map:
                char_map[char] += 1
        #{k:1, q:1, e:2, p:1}
        res = ""
        for k,freq in char_map.items():
            res += k*freq
        #res = "kqeep"
        for char in s:
            if char not in char_map:
                res += char
        return res
        
                