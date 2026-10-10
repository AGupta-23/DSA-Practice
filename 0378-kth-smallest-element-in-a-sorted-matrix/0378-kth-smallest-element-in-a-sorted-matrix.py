class Solution:
    def isPossible(self,n,matrix,k,mid):
        row = n-1
        col = 0
        count = 0

        while (row>=0 and col<n):
            if matrix[row][col]<=mid:
                count += (row+1)
                col += 1
            else: row-=1
        if count >= k: return True
        else: return False
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        ans = 0
        while(low<=high):
            mid = (low+high)//2

            if self.isPossible(n,matrix,k,mid):
                ans = mid
                high = mid -1
            else: low = mid + 1
        return ans

