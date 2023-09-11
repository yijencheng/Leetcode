#https://www.youtube.com/watch?v=pkiJyNijgBw


# wrong!!  >>> First time cannot sell
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        init, buy, hold = 0, 0,0
        for price in prices:
            init,buy,hold  = max(init, hold), max(init-price, buy), max(buy+price, hold)
        return max(init, buy,hold)



#good!
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        init, buy, sell = 0, -prices[0],0
        for price in prices[1:]:
            init,buy,sell  = max(init, sell), max(init-price, buy), buy+price, sell
        return max(init, buy,sell)

