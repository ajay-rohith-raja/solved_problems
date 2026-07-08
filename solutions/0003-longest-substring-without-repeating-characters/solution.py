class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=0
        b=0
        
        arr=[]
        max_len = 0
        while b<len(s):
            l=s[a]
            r=s[b]
            if r not in arr:
                arr.append(r)
                max_len = max(max_len , len(arr))
                b+=1
            elif(r in arr):
               
                arr.remove(s[a])
                a+=1
        return max_len
              
            


        
