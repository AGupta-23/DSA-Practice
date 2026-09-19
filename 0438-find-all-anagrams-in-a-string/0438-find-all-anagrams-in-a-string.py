class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        k = len(p)
        n = len(s)
        countP, countS = {}, {}
        ans = []

        if k>n: return []

        for i in range(0,k):
            countP[p[i]] = countP.get(p[i], 0) + 1
            countS[s[i]] = countS.get(s[i], 0) + 1
        if countP == countS: 
            ans.append(0)

        l = 0
        for r in range(k,n):
            countS[s[r]] = countS.get(s[r], 0) + 1
            countS[s[l]] -= 1

            if countS[s[l]] == 0: 
                countS.pop(s[l])
            l+=1

            if countP == countS: 
                ans.append(l)
        return ans

        