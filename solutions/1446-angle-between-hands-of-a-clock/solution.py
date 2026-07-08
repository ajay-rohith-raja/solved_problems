class Solution:
    def angleClock(self, h: int, m: int) -> float:
        if h==12:
            h=0
        b=abs(30*h - 5.5*m)
        return float(min(b,360-b))
        
