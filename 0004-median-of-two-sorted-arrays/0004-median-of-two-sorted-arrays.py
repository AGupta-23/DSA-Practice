class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)
        arr = []

        while(i < m and j < n):
            if nums1[i]<=nums2[j]:
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        
        while (i<m):
            arr.append(nums1[i])
            i+=1
        while (j<n):
            arr.append(nums2[j])
            j+=1
        
        q = len(arr)
        if q%2 == 1:
            return arr[q//2]
        else:
            return (arr[(q//2)-1] + (arr[q//2]))/2
        