class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #inf = infinity, so any price will be smaller
        min_price = float('inf')
        max_price = 0   
        
        for price in prices:
            max_price = max(max_price, price - min_price)
            min_price = min(min_price, price)

        return max_price