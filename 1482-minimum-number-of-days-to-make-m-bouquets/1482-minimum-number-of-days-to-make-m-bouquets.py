class Solution:
    def isvalid(self, nums, m, k, mid):
        count = 0
        bouquet = 0
        for num in nums:
            if num<=mid:
                count+=1
            else:
                bouquet += count//k
                count = 0
        bouquet += count//k
        if bouquet>=m:
            return True
        else: False

    def minDays(self, nums: list[int], m: int, k: int) -> int:
        ans = -1
        l = min(nums)
        h = max(nums)
        while(l<=h):
            mid = (l+h)//2

            if self.isvalid(nums, m,k,mid):
                ans = mid
                h = mid -1
            else: l = mid + 1
        return ans
        