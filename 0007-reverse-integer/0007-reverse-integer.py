class Solution:
    def reverse(self, x: int) -> int:
        total = 0 
        sign = -1 if x < 0 else 1  
        num = abs(x)

        while num != 0 :
            last_digit = num % 10 
            total = (total*10) + last_digit
            num = num//10
        total *= sign   

        if total < -2**31 or total > 2**31 - 1:
            return 0
            
        return total