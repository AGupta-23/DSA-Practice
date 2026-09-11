class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1  # position where next unique element will be placed

        for i in range(1, len(nums)):
            
            # If current element is different from previous
            # it is a new unique element
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k