class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        hasharray = [0] * 3
        count = 0
        l = 0
        for r in range(0,n):
            hasharray[ (ord(s[r]) - ord('a')) ] += 1

            while hasharray[0]>0 and hasharray[1]>0 and hasharray[2]>0 :
                count += (n-r)
                
                hasharray[ord(s[l]) - ord('a')] -= 1
                l+=1
        return count

        