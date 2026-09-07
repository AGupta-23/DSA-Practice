class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr = ""

        for char in s:
            if char.isalnum():
                newStr += char.lower()
        reversedStr = newStr[::-1]
        if newStr == reversedStr:
            return True
        else: return False
        