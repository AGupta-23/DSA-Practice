from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        result = [None] * (n - k + 1)

        dq = deque()
        result_index = 0

        for i in range(n):

            # 1. Remove elements outside the window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Window is ready
            if i >= k - 1:
                result[result_index] = nums[dq[0]]
                result_index += 1

        return result