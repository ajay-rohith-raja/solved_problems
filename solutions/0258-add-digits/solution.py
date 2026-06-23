class Solution:

     def cal(self,l,n):
         arr = []
         result=0
         for i in range(l):
            a = n%10
            arr.append(a)
            n = n//10
         for i in arr:
            result = result + i
         return result

        
     def addDigits(self, num: int) -> int:
        length_of_num = len(str(abs(num)))

        res = self.cal(length_of_num,num)
        while len(str(abs(res))) > 1:

            res = self.cal(len(str(abs(res))) , res)
        
        return res


