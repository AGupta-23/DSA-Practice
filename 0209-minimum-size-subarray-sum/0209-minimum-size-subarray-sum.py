class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        mini = float('inf')
        n = len(nums)
        l = 0
        sum = 0

        for r in range(0,n):
            sum += nums[r]
            while sum >= target:
                mini = min(mini, (r-l+1))
                sum -= nums[l]
                l+=1
        if mini == float('inf'): return 0
        return mini
