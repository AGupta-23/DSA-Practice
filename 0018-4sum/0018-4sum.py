class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 3):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):

                # Skip duplicate second numbers
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l = j + 1
                r = n - 1

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])

                        # Skip duplicates
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1

                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1

                        l += 1
                        r -= 1

                    elif total < target:
                        l += 1

                    else:
                        r -= 1

        return ans