class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        freq = [0] * 26
        maxfreq = 0
        l = 0
        for r in range(0, n):

                index = ord(s[r]) - ord('A')
                freq[index] += 1

                maxfreq = max(maxfreq, freq[index])
                window = r-l+1
                replacement = window - maxfreq

                if replacement > k:
                    index = ord(s[l]) - ord('A')
                    freq[index] -= 1
                    l+=1

                if replacement <= k:
                    ans = max(ans, window)

        return ans
        