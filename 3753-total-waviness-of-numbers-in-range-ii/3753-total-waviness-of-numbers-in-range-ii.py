class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def solve(n: int) -> int:
            if n < 100:
                return 0
            
            limit_str = str(n)
            length = len(limit_str)
            memo = {}
            
            def dp(idx: int, tight: bool, leading_zero: bool, last: int, prev: int) -> tuple[int, int]:
                if idx == length:
                    return 1, 0

                state_key = (idx, tight, leading_zero, last, prev)

                if state_key in memo:
                    return memo[state_key]
                
                max_digit = int(limit_str[idx]) if tight else 9
                res_count = 0
                res_waviness = 0
                
                for d in range(max_digit + 1):
                    next_tight = tight and (d == max_digit)
                    next_leading_zero = leading_zero and (d == 0)
                    waviness_contribution = 0
                    
                    if not leading_zero and last != -1 and prev != -1:
                        if last > prev and last > d:
                            waviness_contribution = 1
                        elif last < prev and last < d:
                            waviness_contribution = 1
                            
                    if next_leading_zero:
                        next_count, next_waviness = dp(idx + 1, next_tight, True, -1, -1)
                    else:
                        next_count, next_waviness = dp(idx + 1, next_tight, False, d, last)
                        
                    res_count += next_count
                    res_waviness += next_waviness + (waviness_contribution * next_count)
                    
                memo[state_key] = (res_count, res_waviness)
                return res_count, res_waviness

            return dp(0, True, True, -1, -1)[1]
            
        return solve(num2) - solve(num1 - 1)