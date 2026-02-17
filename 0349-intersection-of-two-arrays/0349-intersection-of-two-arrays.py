class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        less  = 0
        
        if nums1 < nums2:
            for n in nums1:
                if n in nums2:
                    ans.append(n)
        
        else:
            for n in nums2:
                if n in nums1:
                    ans.append(n)
        
        return list(set(ans))
