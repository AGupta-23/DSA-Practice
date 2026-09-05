class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        length = 0

        hash_set = set(nums)

        for num in hash_set:
            if num-1 not in hash_set: 
                x = num
                count = 1
                while (x+1) in hash_set:
                    count += 1
                    x += 1
                length = max(length, count)
        return length