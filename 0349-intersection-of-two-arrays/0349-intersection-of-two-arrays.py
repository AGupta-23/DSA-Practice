class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n = len(nums1)
        m = len(nums2)
        ans = []

        for x in nums1:
            if x in nums2 and x not in ans:
                ans.append(x)
        return ans
                
        