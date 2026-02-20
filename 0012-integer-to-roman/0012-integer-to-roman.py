class Solution:
    def intToRoman(self, num: int) -> str:
        nums =list(str(num))
        n=len(nums)
        
        # [3,7,4,9]
        result=[]
        
        roman_dict={"M":1000,'D':500,'C':100,'L':50,'X':10,'V':5,"I":1,}
        num_9_4={9:"IX",4:'IV',40:'XL',90:'XC',400:"CD",900:"CM"}
        not_multip=set("VLD")
        for i  in range(len(nums)-1,-1,-1):
            cur_num=int(nums[i]) * 10 **(n-i-1)
            nums[i]=cur_num
        for m in nums:
            if m in num_9_4:
                result.append(num_9_4[m])
            else:
                while m >0:
                    for key,val in roman_dict.items():
                        if m-val>=0:
                            result.append(key)
                            m -=val
                            break
                    
        return "".join(result)