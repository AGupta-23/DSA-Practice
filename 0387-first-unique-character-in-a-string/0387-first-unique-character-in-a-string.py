class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]]=-1
            else: count[s[i]]=i
        for char in count:
            if count[char] != -1: 
                return count[char]
        return -1
        