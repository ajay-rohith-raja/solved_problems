class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        sum = 0
        for i in str(n):
            mul = mul * int(i)
            sum = sum + int(i)
        return mul-sum
            
