class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        minimum = prices[0]
        maxProfit = 0
        Profit = 0

        for price in prices:
            minimum = min(minimum, price)
            profit = price - minimum 

            if(profit > maxProfit):
                maxProfit = profit
            
        return maxProfit
            
