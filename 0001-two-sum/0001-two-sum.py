class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        hash_map = {}  # empty dict creation

        for i in range(0,n):
            remaining = target - nums[i]

            if remaining in hash_map:
                return[hash_map[remaining], i]
            hash_map[nums[i]] = i


        