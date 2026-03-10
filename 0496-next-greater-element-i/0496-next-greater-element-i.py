class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater = defaultdict(lambda : -1) 

        for n in nums2:
            while stack and stack[-1] < n:
                greater[stack.pop()] = n
            stack.append(n)

        ans = []
        for n in nums1:
            ans.append(greater[n])     
        return ans 