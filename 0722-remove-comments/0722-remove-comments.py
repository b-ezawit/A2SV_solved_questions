class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        ans = []
        block_comment = False
        for line in source:
            i = 0
            if not block_comment:
                valid_line = []
            while i < len(line):
                if line[i:i+2] == "/*" and not block_comment:
                    block_comment = True
                    i += 1
                elif block_comment and line[i:i+2] == "*/":
                    block_comment = False
                    i += 1
                elif line[i:i+2] == "//" and not block_comment:
                    break
                elif not block_comment:
                    valid_line.append(line[i])
                i +=  1
            if not block_comment and valid_line:
                ans.append("".join(valid_line))
        return ans
            
