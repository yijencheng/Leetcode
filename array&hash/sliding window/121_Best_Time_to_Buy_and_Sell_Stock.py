# "why buy high(l), when can buy lower(r)? "

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_buy = prices[0]
        for p in prices:
            max_profit = max(max_profit, p-lowest_buy)
            lowest_buy = min(lowest_buy, p)
        return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        ans = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                ans = max(ans, prices[r]-prices[l])
        return ans