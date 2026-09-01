class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        map = {}

        for num in nums:
            map[num]= map.get(num,0) + 1
            if map[num]>n/2:
                return num
        