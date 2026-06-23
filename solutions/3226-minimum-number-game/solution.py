class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        while len(nums)!=0:
            min_a = min(nums)
            nums.remove(min_a)
            min_b = min(nums)
            nums.remove(min_b)

            arr.append(min_b)
            arr.append(min_a)
        
        return arr


