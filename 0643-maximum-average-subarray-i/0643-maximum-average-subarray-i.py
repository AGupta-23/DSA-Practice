class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        n = len(nums)

        # Step 1: Calculate the sum of the first window
        window_sum = sum(nums[:k])

        # Store the maximum sum found so far
        max_sum = window_sum

        # Step 2: Slide the window
        for i in range(k, n):

            # Add the new element entering the window
            # Remove the old element leaving the window
            window_sum += nums[i] - nums[i - k]

            # Update maximum sum
            max_sum = max(max_sum, window_sum)

        # Convert maximum sum to maximum average
        return max_sum / k


        