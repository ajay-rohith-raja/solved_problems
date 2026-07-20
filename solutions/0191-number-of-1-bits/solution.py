class Solution:
    def hammingWeight(self, n: int) -> int:

        c =0
        while n > 0:
            t = n % 2
            if (t == 1):
                c = c + 1
            n = n // 2

        return c
        
