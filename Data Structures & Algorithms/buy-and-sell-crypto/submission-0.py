class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)): # O(n)
            for j in range(i + 1, len(prices)): #O(n)
                if prices[j] - prices[i] > profit and prices[j] > prices[i]: 
                    profit = prices[j] - prices[i]
        return profit
        