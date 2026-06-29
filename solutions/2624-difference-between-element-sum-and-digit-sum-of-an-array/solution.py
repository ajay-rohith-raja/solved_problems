class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele = 0
        for i in nums:
            ele = ele + i
        
        dig = 0
        for j in nums:
            if len(str(j)) > 1 :
                x = j
                z=50
                res=0
                while z!=0:
                    last = x%10
                    x = x//10
                    z=x
                    res=res+last
                dig = dig+res
            else:
                dig = dig+j
        
        return abs(ele-dig)




