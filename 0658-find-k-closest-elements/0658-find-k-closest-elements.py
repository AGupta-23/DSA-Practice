class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l = 0
        h = n-k

        while(l<h):
            mid = l + (h-l)//2

            if (x - arr[mid]) > (arr[mid + k] - x):
                l = mid + 1
            else: h = mid
        return arr[l:(l+k)]