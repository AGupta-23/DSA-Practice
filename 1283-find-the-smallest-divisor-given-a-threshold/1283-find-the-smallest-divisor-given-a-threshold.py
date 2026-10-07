class Solution:
    def isValid(self, n, nums , mid, threshold):
        sum = 0
        for num in nums:
            if num % mid == 0: 
                x = num//mid
            elif num % mid != 0:
                x = (num//mid) + 1
            
            if (sum + x)<= threshold:
                sum += x
            else: return False
        return True
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        n = len(nums)
        l=1
        h = max(nums)
        ans = 0
        while(l<=h):
            mid = (l+h)//2
            if self.isValid(n,nums, mid, threshold):
                ans = mid
                h = mid - 1
            else: l = mid + 1
        return ans