class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        c = 0
        arr=[]
        for i in words:
            
            if x in i:
                arr.append(c)
            c = c+1
        
        return arr
                

        
