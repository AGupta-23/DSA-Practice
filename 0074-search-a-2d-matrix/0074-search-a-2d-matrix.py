class Solution:

    def searchTarget(self, matrix:list[list[int]], target:int, midRow:int)-> bool:
        l =0
        h= len(matrix[0])
        while(l<=h):
            m=(l+h)//2
            if matrix[midRow][m]==target:
                return True
            elif matrix[midRow][m]<target:
                l=m+1
            else: h=m-1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        l = 0
        h = m-1

        while ( l<=h ):
            mid = (l+h) //2

            if matrix[mid][0] <= target <= matrix[mid][n-1]:
                return self.searchTarget(matrix,target,mid)
            
            if matrix[mid][n-1] < target:
                l = mid + 1
            else: 
                h = mid - 1
        return False

        