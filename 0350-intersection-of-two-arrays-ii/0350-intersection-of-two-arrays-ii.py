class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #BRUTE SOL -- CHANGING NUMS2

        n = len(nums1)
        m = len(nums2)
        result = []
        count = {}

        for x in nums1:
            count[x] = count.get(x,0)+1
        for y in nums2:
            if y in count and count[y]>0:
                result.append(y)
                count[y]-=1
        return result
