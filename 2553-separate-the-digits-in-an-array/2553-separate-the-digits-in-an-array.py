class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_str = "".join(list(map(str,nums)))
        return [int(c) for c in nums_str]