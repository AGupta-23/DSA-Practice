class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:

            # Partition nums1
            cut1 = (left + right) // 2

            # Partition nums2
            cut2 = (m + n + 1) // 2 - cut1

            # Elements just outside the partitions
            l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            r1 = float('inf') if cut1 == m else nums1[cut1]

            l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            r2 = float('inf') if cut2 == n else nums2[cut2]

            # Correct partition
            if l1 <= r2 and l2 <= r1:

                # Odd total length
                if (m + n) % 2 == 1:
                    return max(l1, l2)

                # Even total length
                return (max(l1, l2) + min(r1, r2)) / 2

            # We need to move partition in nums1 right
            elif l1 > r2:
                right = cut1 - 1

            # We need to move partition in nums1 left
            else:
                left = cut1 + 1