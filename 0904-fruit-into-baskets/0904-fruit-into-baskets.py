class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        l = 0
        maxi = 0
        count = {}

        for r in range(0,n):
            count[fruits[r]] = count.get(fruits[r], 0) + 1

            if len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l+=1
            
            if len(count) <= 2:
                maxi = max(maxi, (r-l+1))
        return maxi

        