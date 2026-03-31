class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy, sell = 0, 1
        maxP = 0

        while sell < len(prices):
            if prices[buy] > prices[sell]: 
                buy = sell

            if prices[sell] > prices[buy]: 
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
            sell += 1
        
        return maxP






        