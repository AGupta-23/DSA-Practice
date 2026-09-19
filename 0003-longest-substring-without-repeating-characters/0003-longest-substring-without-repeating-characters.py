class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        maxi = 0
        left , right = 0,0 
        my_dict = {}
        
        while right < n:
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]] + 1)
            length = right - left + 1
            my_dict[s[right]] = right
            maxi = max(maxi, length)
            right+=1
        return maxi
        