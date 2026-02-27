class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        maP = defaultdict(int)
        for i,c in enumerate(s):
            maP[c] = i

        size = end = 0
        output = []

        for i,c in enumerate(s):
            size += 1
            end = max(end , maP[c])#end == 8
            if i==end:
                output.append(size)
                size = 0
        
        return output



            
        