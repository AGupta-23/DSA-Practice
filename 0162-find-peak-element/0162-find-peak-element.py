class Solution:
    def findPeakElement(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        if arr[0]>arr[1]:
            return 0
        for i in range(1,n-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                return i
        else: 
            return n-1