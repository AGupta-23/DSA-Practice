class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        low = 1
        high = n-1
        while(low<=high):
            mid = (low+high)//2

            count = 0
            for i in range(0,n):
                if nums[i]<=mid:
                    count+=1
            
            if count<=mid:
                low = mid+1
            else:
                ans = mid
                high = mid-1
        return ans

        