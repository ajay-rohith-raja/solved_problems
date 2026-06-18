class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i=="[" or i =="(" or i=="{":
                stack.append(i)
            else:
                if (i=="]" or i==")" or i=="}") and len(stack) < 1:
                    return False
                elif(i=="]"):
                    a = stack.pop()
                    if(a!="["):
                        return False
                elif(i=="}"):
                    a = stack.pop()
                    if(a!="{"):
                        return False
                elif(i==")"):
                    a=stack.pop()
                    if(a!="("):
                        return False
        if stack:
            return False
        return True



        
