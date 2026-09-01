class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if candidate == num:
                count+=1
            else: # candidate!=num
                count-=1
        # return candidate

        #verification
        count = 0
        for num in nums:
            if num == candidate:
                count+=1
            if count > n//2:
                return num

        