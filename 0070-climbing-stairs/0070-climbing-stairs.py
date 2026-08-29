class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for i in range(2, n + 1):
            current = one + two
            two = one
            one = current

        return one
        