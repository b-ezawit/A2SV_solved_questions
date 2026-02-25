class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citations = [3,0,6,1,5]
        # citations = [0,1,3,5,6]
        max_candidate = 0
        citations.sort()
        n = len(citations)
        for i in range(n):
            if n - i <= citations[i]:
                return n-i

        return 0