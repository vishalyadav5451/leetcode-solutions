class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) :
            return False

        curr_s = s + s
        if goal in curr_s :
                return True
        
        return False
       

