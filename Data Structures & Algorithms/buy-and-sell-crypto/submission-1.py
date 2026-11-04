class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, profit = 0, 0

        for R in range(len(prices)):
            diff = prices[R] - prices[L]
            if diff < 0:
                L = R
            profit = max(profit, diff)

        return profit
            