class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        map1 = {}
        for char in s1:
            map1[char] = map1.get(char,0) + 1

        for i in range(0,m-n+1):
            map2 = {}
            for j in range(i,i+n):
                map2[s2[j]] = map2.get(s2[j],0) + 1

                if len(map1) == len(map2):
                    if map1 == map2:
                        return True
        return False

