class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasht = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need not in hasht:
                hasht[nums[i]] = i
            elif need in hasht:
                return [hasht[need],i]


        
        
