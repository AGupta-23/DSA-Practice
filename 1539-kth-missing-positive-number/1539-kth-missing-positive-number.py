class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        n = len(arr)
        low = 0
        high = n-1

        while(low<=high):
            mid = (low + high)//2
            missing = arr[mid] - (mid+1)

            if missing < k:
                low = mid + 1
            else: high = mid - 1
        
        # arr[high] + (more --> (k - missing))
        # missing = arr[high] - (high + 1)
        # missing = arr[high] - (low)
        # arr[high] + k - (arr[high] - low)
        return (k + low)


        