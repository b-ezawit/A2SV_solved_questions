class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ans = [0] * len(s)
        n = len(s)

        for i in range(len(s)):
            char = s[i]
            destination = indices[i]
            ans[destination] = char

        return "".join(ans)