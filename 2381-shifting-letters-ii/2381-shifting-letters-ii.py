class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        
        diff = [0] * (len(s)+1)

        for a,b,d in shifts:
            if d == 1:
                diff[b+1] += 1
                diff[a] -= 1
            else:
                diff[b+1] -= 1
                diff[a] += 1

        res =[ord(c)-ord("a") for c in s]

        cSum = 0
        for i in reversed(range(len(diff))):
            cSum += diff[i]
            res[i-1]= ((res[i-1] + cSum)+26) % 26

        st = [chr(ord("a")+n) for n in res]

        return "".join(st)
