class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        maxi = 0
        count = 0
        vowels = "aeiou"

        for i in range(k):
            if s[i] in vowels:
                count+=1
        maxi = count

        for r in range(k,n):
            if s[r] in vowels:
                count+=1
            if s[r-k] in vowels:
                count-=1
            maxi = max(maxi, count)
        return maxi

        