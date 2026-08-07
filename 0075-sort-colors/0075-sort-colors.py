class Solution:
    def sortColors(self, nums: List[int]) -> None:

        n = len(nums)

        countRed = 0
        countWhite = 0
        countBlue = 0

        # Count 0s, 1s, and 2s
        for i in range(n):
            if nums[i] == 0:
                countRed += 1
            elif nums[i] == 1:
                countWhite += 1
            else:
                countBlue += 1

        y = 0

        # Fill 0s
        for i in range(countRed):
            nums[y] = 0
            y += 1

        # Fill 1s
        for i in range(countWhite):
            nums[y] = 1
            y += 1

        # Fill 2s
        for i in range(countBlue):
            nums[y] = 2
            y += 1
        