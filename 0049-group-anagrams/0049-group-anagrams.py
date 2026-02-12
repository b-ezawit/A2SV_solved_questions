class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = defaultdict(list)

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        
        return [anagram for anagram in anagram_map.values()]