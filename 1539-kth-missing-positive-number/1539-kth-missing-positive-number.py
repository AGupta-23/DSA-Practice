class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        n = len(arr)
        for i in range(0,n):
            if arr[i]<=k:
                k+=1
            else: #when arr[i]>k
                break
        return k
        