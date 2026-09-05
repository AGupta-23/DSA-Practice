class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n = len(nums1)
        m = len(nums2)
        ans = set()

        for i in range(0,n):
            if nums1[i] in nums2:
                ans.add(nums1[i])
        return list(ans)
                
        