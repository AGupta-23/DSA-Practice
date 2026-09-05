class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set2 = set(nums2)
        result = set()

        for x in nums1:
            if x in set2:
                result.add(x)
        return list(result)

                
        