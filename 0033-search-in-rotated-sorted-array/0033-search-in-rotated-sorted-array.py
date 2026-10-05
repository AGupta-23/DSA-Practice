class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l,h = 0, n-1

        while(l<=h):
            mid = (l+h) //2

            if nums[mid] == target: return mid
            if (nums[l] <= nums[mid]):
                #means left half is sorted
                if (nums[l]<= target and target<=nums[mid]):
                    h = mid -1
                else: l = mid + 1
            else:
                if (nums[mid]<= target and target<=nums[h]):
                    l = mid + 1
                else: h = mid - 1
        return -1

        