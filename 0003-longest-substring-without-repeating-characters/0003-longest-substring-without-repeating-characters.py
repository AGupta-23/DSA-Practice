class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        maxi = 0

        for i in range(0,n):
            hash_set = set()
            for j in range(i,n):
                if s[j] in hash_set: break
                else:
                    hash_set.add(s[j])
                    windowLen = j-i+1
                    maxi = max(maxi, windowLen)
        return maxi
        