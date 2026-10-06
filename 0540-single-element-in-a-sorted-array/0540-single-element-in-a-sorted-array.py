class Solution:
    def singleNonDuplicate(self, A: List[int]) -> int:
        n = len(A)
        if n== 1: return A[0]
        for i in range(0, n):
            if i == 0 and A[i] != A[i+1]: return A[0]
            if i == n-1 and A[n-1] != A[n-2]: return A[n-1]
            if A[i-1]!=A[i]!=A[i+1]:
                return A[i]
        