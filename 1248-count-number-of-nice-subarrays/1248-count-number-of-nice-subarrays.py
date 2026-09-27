class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def atmost(k):
        
            n = len(nums)
            ans = 0
            l = 0
            odd = 0

            for r in range(n):
                if nums[r] % 2 == 1:
                    odd += 1
                while odd>k:
                    if nums[l] % 2 == 1:
                        odd -= 1
                    l+=1
                ans += r-l+1
            return ans

        return atmost(k) - atmost(k-1)
                
