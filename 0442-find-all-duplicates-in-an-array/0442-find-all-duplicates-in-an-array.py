class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #brute force:
        numsCount = Counter(nums)
        return [k for k in numsCount if numsCount[k]==2]
        