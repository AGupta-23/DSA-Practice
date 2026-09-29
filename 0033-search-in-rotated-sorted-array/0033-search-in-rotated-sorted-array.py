class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[l] <= nums[mid]:

                # Target lies in the sorted left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # Right half is sorted
            else:

                # Target lies in the sorted right half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1