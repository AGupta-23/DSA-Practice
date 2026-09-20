class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        freq1 = [0] * 26
        freq2 = [0] * 26

        for char in s1:
            freq1[ord(char) - ord('a')] += 1
        
        l = 0
        for r in range(0,m):
            freq2[ord(s2[r]) - ord('a')] += 1
            
            if r-l+1 > len(s1):
                freq2[ord(s2[l]) - ord('a')] -= 1
                l+=1

            if (r-l+1) == len(s1):
                if freq1 == freq2:
                    return True
        return False



