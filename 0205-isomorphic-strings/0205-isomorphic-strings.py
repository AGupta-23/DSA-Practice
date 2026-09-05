class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        map1 = {}
        map2 = {}

        for i in range(0, len(s)):
            x = s[i]
            y = t[i]

            if x in map1 and map1[x] != y:
                return False
            if y in map2 and map2[y] != x:
                return False

            map1[x]=y
            map2[y]=x

            # i+=1
        return True
                
        