class Solution:
    def findMin(self, arr: list[int]) -> int:
        n = len(arr)
        l,h = 0, n-1
        ans = float(inf)

        while(l<=h):
            m = (l+h)//2

            #slight more optimization --> low to high all is sorted - whenever reached the rotated point --> index low holds the minimum 
            if (arr[l] <= arr[h]):
                ans = min(ans, arr[l])
                break

            if (arr[l] <= arr[m]): 
                #left half is sorted
                ans = min(ans, arr[l])
                l = m + 1
            else:
                #right half is sorted
                ans = min(ans, arr[m])
                h = m - 1
        return ans
