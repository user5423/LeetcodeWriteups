class Solution:
    def maxProfit(self, prices: List[int]) -> int:
	self.twoPassSolution(prices)
	self.onePassSolution(prices)

    def twoPassSolution(self, prices: List[int]) -> int:
        profit = 0
        ## we need to find a min and max
        ## where indexof(min) < indexof(max)
        
        if len(prices) == 1:
            return profit
        
        maxValues = {}
        bestMax = prices[-1]
        maxValues[len(prices)-1] = bestMax
        
        for i in range(len(prices)-2,-1,-1):
            bestMax = max(bestMax, prices[i])
            maxValues[i] = bestMax
            
        for i in range(len(prices)-1):
            profit = max(profit, maxValues[i+1]-prices[i])
            
        return profit
            

    def onePassSolution(self, prices: List[int]) -> int:
        bestProfit = 0
        lowestBuy = prices[0]
        for price in prices[1:]:
            bestProfit = max(price - lowestBuy, bestProfit)
            lowestBuy = min(lowestBuy, price)
            
        return bestProfit
        
        
