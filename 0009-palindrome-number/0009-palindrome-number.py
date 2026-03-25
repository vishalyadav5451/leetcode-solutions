class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0 
        num = x 
        if x==0 : return True
        while num > 0 :
            last_d = num % 10
            res = (res*10) + last_d
            num = num//10
        
            if x == res : 
                return True
        
        return False