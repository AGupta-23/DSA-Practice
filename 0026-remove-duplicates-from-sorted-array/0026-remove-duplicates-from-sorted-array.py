class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        j = 1

        while (j<n):
            if nums[j] != nums[i]:
                i+=1
                nums[i], nums[j] = nums[j], nums[i]
            j+=1
        return i+1
        