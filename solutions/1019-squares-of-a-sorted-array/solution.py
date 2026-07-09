class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in nums:
            arr.append(abs(i)**2)
        return sorted(arr)

        
