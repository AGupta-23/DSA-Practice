from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        dq=deque()
        result=[]

        for i in range(0,n):
            #1. Remove all that are outside window range in dq
            if dq and dq[0]<=i-k:
                dq.popleft()
            #2. Remove smaller unwanted elements in deque
            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()
            #3. append the ith index in dq 
            dq.append(i)
            #4. if window formed - sized k - add the dq.front indx value into element in result
            if i>=k-1:
                result.append(nums[dq[0]])
        return result