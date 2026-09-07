class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n-1

        while(l<r):

            while l<r and not self.func(s[l]): 
                l+=1

            while l<r and not self.func(s[r]): 
                r-=1

            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True

    def func(self, char):
        if (ord('a')<=ord(char)<=ord('z') or
            ord('A')<=ord(char)<=ord('Z') or
            ord('0')<=ord(char)<=ord('9')): 
            return True
        else: return False

        
        