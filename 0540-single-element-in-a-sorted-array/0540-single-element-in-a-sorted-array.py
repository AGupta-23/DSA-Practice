class Solution:
    def singleNonDuplicate(self, A: List[int]) -> int:
        n = len(A)
        if n== 1: return A[0]

        l=0
        h=n-1
        while(l<=h):
            mid = (l+h)//2
            if mid == 0 and A[mid] != A[mid+1]: return A[0]
            if mid == n-1 and A[n-1] != A[n-2]: return A[n-1]
            if A[mid-1]!=A[mid]!=A[mid+1]:
                return A[mid]

            if mid % 2 == 0:
                # mid is at an even position - both side have even search spaces
                if A[mid]==A[mid-1]:
                    h = mid -1
                else: l = mid + 1
            else:
                # mid is at an odd position so - both sides has odd search spaces
                    if A[mid]==A[mid-1]:
                        l = mid+1
                    else: h = mid -1
        return -1

        