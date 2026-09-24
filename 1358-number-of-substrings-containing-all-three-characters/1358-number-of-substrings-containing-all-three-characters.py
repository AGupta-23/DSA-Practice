class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        hashset = {}
        count = 0
        l = 0
        for r in range(0,n):
            hashset[s[r]] = hashset.get(s[r], 0) + 1
            while len(hashset) == 3:
                count += n-r

                hashset[s[l]] -= 1
                if hashset[s[l]] == 0: del hashset[s[l]]
                l+=1

        return count

        