class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        arr = []
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                arr.append(matrix[i][j])

        arr.sort()

        return arr[k - 1]