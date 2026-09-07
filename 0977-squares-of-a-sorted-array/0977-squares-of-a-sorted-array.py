class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        left = 0
        right = n-1

        for i in range(n-1,-1,-1):
            a = (nums[left]**2)
            b = (nums[right]**2)

            if a>b:
                result[i]=a
                left+=1
            else:
                result[i]=b
                right-=1
        return result
