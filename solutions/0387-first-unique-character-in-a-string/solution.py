class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=0
        for i in s:
            t = s.count(i)
            f = s.count(i)
            if f==1:
                return c
            c=c+1
        if t>1:
            return -1
        
