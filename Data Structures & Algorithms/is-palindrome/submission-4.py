class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while right-left>0: 
            while not s[left].isalnum() and left<len(s)-1: left += 1
            while not s[right].isalnum() and right>0: right -= 1
            if left>=len(s)-1 or right<0: continue
            if s[left].lower() != s[right].lower(): return False
            left += 1; right -= 1
        return True