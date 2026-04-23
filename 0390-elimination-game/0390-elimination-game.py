class Solution:
    def lastRemaining(self, n: int) -> int:
        '''arr = [num for num in range(1,n+1)]
        left_to_right = True
        while len(arr) > 1:
            new_arr = []
            if left_to_right:
                for i in range(1,len(arr),2):
                    new_arr.append(arr[i])
            else:
                for i in range(len(arr)-2,-1,-2):
                    new_arr.append(arr[i])
                new_arr.reverse()
            arr = new_arr
            left_to_right = not left_to_right
        return arr[0]'''

        # 1 2 3 4 5 6 7 8 9
        #           h
        left = True  
        remaining = n #0
        step = 1 #8
        head = 1 #6
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            step *= 2  
            remaining //= 2
            left = not left 

        return head

        
    


        