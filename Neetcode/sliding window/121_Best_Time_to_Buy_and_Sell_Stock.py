# "why buy high(l), when can buy lower(r)? "

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