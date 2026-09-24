class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        hashset = {'a':0, 'b':0, 'c':0}
        count = 0
        l = 0
        for r in range(0,n):
            hashset[s[r]] = hashset.get(s[r], 0) + 1

            while hashset['a']>0 and hashset['b']>0 and hashset['c']>0 :
                count += (n-r)
                
                hashset[s[l]] -= 1
                l+=1
        return count

        