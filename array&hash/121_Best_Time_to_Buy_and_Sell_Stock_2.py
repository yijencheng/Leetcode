if buy p0:
- if p1 > p0: sell. (then what's the buy_price? can set to current_price, which is high*)
- if p1 < p0: we should buy next instead of now >> update buy_price

* can set to zero instead ? >> NO! since 下一個有可能會更高，現在也有可能是buy_price


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy_price = prices[0]
        for p in prices:
            if p > buy_price:
                ans += (p-buy_price)
            buy_price = p
        return ans