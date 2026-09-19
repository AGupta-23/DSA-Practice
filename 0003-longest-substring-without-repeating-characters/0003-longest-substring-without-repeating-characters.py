class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        maxi = 0

        for i in range(0,n):
            hash_set = set()
            for j in range(i,n):
                if s[j] in hash_set: break
                hash_set.add(s[j])
                maxi = max(maxi, j-i+1)
        return maxi
        