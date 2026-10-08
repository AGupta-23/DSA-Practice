class Solution:
    def isPossible(self, arr, m , maxpossibleDist,n):
        balls = 1
        lastpos=arr[0]
        for i in range(1,n):
            if arr[i] - lastpos >= maxpossibleDist:
                lastpos = arr[i]
                balls += 1
        if balls>=m: return True
        else: return False

    def maxDistance(self, arr: list[int], m: int) -> int:
        arr.sort()
        n=len(arr)
        low = 1
        high = arr[n-1]-arr[0]
        ans = -1
        while(low<=high):
            mid = (low+high)//2

            if self.isPossible(arr,m,mid,n):
                ans = mid
                low = mid + 1
            else: high = mid - 1
        return ans
