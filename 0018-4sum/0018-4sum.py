class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        result_set = set()

        for i in range(0,n):
            for j in range(i+1, n):
                hash_set = set()
                for k in range(j+1,n):
                    fourth = target - (nums[i]+nums[j]+nums[k])
                    if fourth in hash_set:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        result_set.add(tuple(temp))
                    hash_set.add(nums[k])
        return list(list(ans) for ans in result_set)
    
                