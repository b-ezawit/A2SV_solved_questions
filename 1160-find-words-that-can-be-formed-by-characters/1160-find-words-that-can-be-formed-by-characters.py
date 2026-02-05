class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        


# words = ["cat","bt","hat","tree"], chars = "atach"

        charsCount = Counter(chars) #charsCount = {'a':2,'t':1,'c':1,'h':1}
        ans = 0
        for string in words:
            stringCount = Counter(string)#stringCount = {'c':1,'a':1,'t':1}
            for ch in stringCount:
                if (stringCount[ch] > charsCount[ch]):
                    break
            else:
                ans += len(string)
        return ans

            
