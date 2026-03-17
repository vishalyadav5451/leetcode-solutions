class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = list(dict.fromkeys(nums))
        
        for i in range(len(n)):
            nums[i]= n[i]
        return len(n)


