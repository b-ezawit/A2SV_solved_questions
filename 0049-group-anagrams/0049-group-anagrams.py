class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []

        hash = defaultdict(list)

        for s in strs:
            sorted_s = tuple(sorted(s))
            hash[sorted_s].append(s)
        #{'aet':['eat','ate','tea']}

        for values in hash.values():
            ans.append(values)

        return ans

