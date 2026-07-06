class Solution(object):
    def toLowerCase(self, s):
        ans = ""
        for i in range(len(s)):
            if s[i].isupper():
                ans = ans + s[i].lower()
            else:
                ans = ans + s[i]
        return ans        
