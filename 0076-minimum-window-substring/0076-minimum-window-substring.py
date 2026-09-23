class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(t)
        n = len(s)
        sIndex = -1
        minLen = float(inf)
        hashmap = {}
        l = 0
        count = 0

        for char in t:
            hashmap[char] = hashmap.get(char, 0) + 1

        for r in range(0,n):

            if hashmap.get(s[r],0) > 0:
                count+=1
            hashmap[s[r]] = hashmap.get(s[r], 0) - 1
            while count == m:
                if (r-l+1) < minLen:
                    minLen = r-l+1
                    sIndex = l
                
                hashmap[s[l]] += 1
                if hashmap[s[l]] > 0:
                    count -= 1
                
                l+=1

        if sIndex == -1:
            return ""
        return s[sIndex: sIndex + minLen]

        