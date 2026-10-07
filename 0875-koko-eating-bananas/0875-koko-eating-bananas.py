class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        h_speed = max(piles)

        while l <= h_speed:
            mid = (l + h_speed) // 2

            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                # mid works, but maybe a smaller speed also works
                h_speed = mid - 1
            else:
                # mid is too slow
                l = mid + 1

        return l