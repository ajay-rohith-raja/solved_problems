class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        t1 = 0
        for i in sentences:
            a = i
            t = a.count(" ")
            if t>t1:
                t1 = t
            
        return t1+1
        
