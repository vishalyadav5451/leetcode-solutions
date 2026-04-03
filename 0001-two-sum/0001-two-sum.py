class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}
        for i in range (len(nums)):
            sum = target - nums[i] 
            if sum in hash_map :
                return [hash_map[sum] , i]
            
            hash_map[nums[i]] = i