class Solution():
    def maxProfit(self, prices):
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
        return profit
x=Solution()
prices = [100, 180, 260, 310, 40, 535, 695]
prices1 = [4, 2, 2, 2, 4]
print(x.maxProfit(prices))
print(x.maxProfit(prices1))