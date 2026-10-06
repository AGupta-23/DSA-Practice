# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        n = mountainArr.length()

        # 1. Find peak
        l = 0
        h = n - 1

        while l < h:
            mid = (l + h) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                h = mid

        peak = l

        # 2. Binary search increasing part
        l = 0
        h = peak

        while l <= h:
            mid = (l + h) // 2
            val = mountainArr.get(mid)

            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else:
                h = mid - 1

        # 3. Binary search decreasing part
        l = peak + 1
        h = n - 1

        while l <= h:
            mid = (l + h) // 2
            val = mountainArr.get(mid)

            if val == target:
                return mid
            elif val > target:
                l = mid + 1
            else:
                h = mid - 1

        return -1

        