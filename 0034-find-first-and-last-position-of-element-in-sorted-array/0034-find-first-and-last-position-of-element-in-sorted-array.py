class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        # Find first occurrence
        l = 0
        r = len(nums) - 1
        first = -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                first = mid
                r = mid - 1       # go LEFT
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        # Find last occurrence
        l = 0
        r = len(nums) - 1
        last = -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                last = mid
                l = mid + 1       # go RIGHT
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return [first, last]