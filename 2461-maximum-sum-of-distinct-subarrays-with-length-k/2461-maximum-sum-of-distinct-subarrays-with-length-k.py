class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        window_sum = 0
        max_sum = 0

        left = 0

        for right in range(len(nums)):
            # Add current element
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            window_sum += nums[right]

            # Keep window size <= k
            if right - left + 1 > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                window_sum -= nums[left]
                left += 1

            # Window has size k and all elements are distinct
            if right - left + 1 == k and len(freq) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum