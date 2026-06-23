class Solution:
    def pali(self,s):
        a = ""
        for i in s:
            a = i + a
        if a==s:
            return 1
        else: 
            return 0
            

    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if(self.pali(i)):
                return i
            
        return ""
        
