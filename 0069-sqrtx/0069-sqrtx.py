class Solution:
    def mySqrt(self, x: int) -> int:
        l , r = 1 , x//2
        ans = 0
        if x == 1 :
            return 1

        while l <= r :
            mid = (l+r)//2 

            if mid*mid <= x :
                l = mid + 1
                ans = mid 
            else :
                r = mid -1
                

        return ans
