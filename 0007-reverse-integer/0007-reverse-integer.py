class Solution:
    def reverse(self, x: int) -> int:
        total = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0 :
            l_d = x%10
            total = (total*10) + l_d
            x = x//10

        total *= sign 

        if total < -(2**31) or total > (2**31-1) :
            return 0

        return total
