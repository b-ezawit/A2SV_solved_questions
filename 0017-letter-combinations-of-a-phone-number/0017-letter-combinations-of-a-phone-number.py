class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap = {
            2:"abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        ans = []
        maxlen = 1
        for num in digits:
            maxlen *= len(hmap[int(num)])

        def backtrack(indx,path):
            if len(path) == len(digits):
                if path not in ans:
                    ans.append("".join(path[:]))
                return 

            for letter in hmap[int(digits[indx])]:
                path.append(letter)
                backtrack(indx+1,path)
                path.pop()
        

        backtrack(0,[])
        return ans



                

        