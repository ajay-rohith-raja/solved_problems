class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        c=0
        for i in alphabets:
            if i in sentence:
                c=c+1
        
        if c==26:
            return True
        else:
            return False
        
