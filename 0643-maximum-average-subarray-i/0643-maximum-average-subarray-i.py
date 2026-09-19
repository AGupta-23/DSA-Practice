class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        sum = 0
        for i in range(0, k):
            sum += nums[i]
        max_avg = sum/k

        for i in range(k, n):
            sum = sum + nums[i] - nums[i-k]
            avg = sum/k
            max_avg = max(avg, max_avg)
        return max_avg


        