class Solution:
    def findPeakElement(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 1: return 0
        if arr[0]>arr[1]: return 0
        if arr[n-1]>arr[n-2]: return n-1

        l = 1
        h = n-2

        while(l<=h):
            mid = (l+h)//2

            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]<arr[mid]:
                l=mid+1
            else: h = mid - 1
        