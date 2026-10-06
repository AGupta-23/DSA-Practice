class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        m = len(accounts)
        n = len(accounts[0])
        richest = 0

        for i in range(0,m):
            sum = 0
            for j in range(0,n):
                sum += accounts[i][j]
            richest = max(richest, sum)
        return richest
        