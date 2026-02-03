class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = float('inf')
        min_str = ""
        
        common_pref = ""
        
        for i in range(len(strs)):
            if min_len > len(strs[i]):
                min_len = len(strs[i])
                min_str = strs[i]
        
        for j in range(min_len):
            for i in range(len(strs)):
                if min_str[j] != strs[i][j]:
                    return common_pref

            common_pref += min_str[j]
        return common_pref
            