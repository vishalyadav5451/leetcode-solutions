class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        if n == 2: return False
        seen = set()
         
        
        while n != 1 and n not in seen :
            seen.add(n)
            res = 0
            while n >  0 :
                last_digit = n % 10
                res = res + (last_digit * last_digit)
                n = n//10

            n = res

        return n ==1