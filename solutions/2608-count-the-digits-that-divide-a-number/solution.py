class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        temp = num
        for i in range(len(str(abs(num)))):
            
            last_num = temp%10
            if num%last_num == 0:
                c = c+1
            temp = temp//10
        
        return c
        
