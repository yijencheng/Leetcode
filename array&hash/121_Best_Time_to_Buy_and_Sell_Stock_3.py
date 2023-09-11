class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy = prices[0]
        oneBuyOneSell = 0
        twoBuy = prices[0]
        twoBuyTwoSell = 0
        for i in range(len(prices)):
            lowest_buy = min(lowest_buy, prices[i])
            oneBuyOneSell = max(oneBuyOneSell, prices[i] - lowest_buy)

            twoBuy = min(twoBuy, prices[i]-oneBuyOneSell) # 找onebuyonesell後的最低點
            # Why prices[i] - oneBuyOneSell ? 假設有A,B兩點
            # - A=3, oneBuyOneSell=2
            # - B=5, oneBuySell=7  >>>  最後是選他，雖然比較高，但是相減的點～prices[i]的距離是兩次買賣的合，
            
            twoBuyTwoSell = max(twoBuyTwoSell, prices[i]- twoBuy)
            print(lowest_buy, oneBuyOneSell, twoBuy,twoBuyTwoSell)
        return max(oneBuyOneSell, twoBuyTwoSell)