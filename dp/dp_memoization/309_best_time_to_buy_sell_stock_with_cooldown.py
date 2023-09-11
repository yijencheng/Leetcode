# two state

# three state
class Solution:
    def maxProfit(self, prices: List[int]) -> int:      
        # init: buy/cool
        # hold: sell/cool
        # cool: cool
        dp={}
        state = ""
        def dfs(i, state):
            if i>=len(prices):return 0
            
            if (i, state) in dp:
                return dp[(i, state)]

            if state == "init":
                dp[(i, state)] = max(dfs(i+1,"hold")-prices[i], dfs(i+1,"init"))
            elif state == "hold":
                dp[(i, state)] = max(dfs(i+1,"cool")+prices[i], dfs(i+1,"hold"))
            elif state == "cool":
                dp[(i, state)] = dfs(i+1,"init")
            else:
                print("error")
                
            return dp[(i, state)]
    
        return dfs(0,"init")


#wrong!!!
[1,2,3,0,2]
{
    (4, False): 2, (4, True): 0, 
    (3, False): 2, (3, True): 2, 
    (2, False): 5, (2, True): 2, #wrong
    (1, False): 7, (1, True): 3, #wrong
    (0, True): 6} #wrong

class Solution:
    def maxProfit(self, prices: List[int]) -> int:      
        #buy->sell/cool
        #cool-> buy/cool
        #sell->cool
        dp={}
        def dfs(i, canBuy):
            if i>=len(prices):return 0
            
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]

            if canBuy:
                buy = dfs(i+1, False) - prices[i]
                cool = dfs(i+1, True)
                dp[(i, canBuy)] = max(buy, cool)
            else:
                sell = dfs(i+1, False)+prices[i]
                cool = dfs(i+1, True)
                dp[(i, canBuy)] = max(sell, cool)
            return dp[(i, canBuy)]
        return dfs(0,True)


{
    (4, False): 2, (4, True): 0, 
    (3, False): 2, (3, True): 2,
    (2, False): 3, (2, True): 2, 
    (1, False): 4, (1, True): 2,
    (0, True): 3
}

state: 
- 並不是buy這個選擇（左） 、是指可以sell/buy的狀態（右）
- 如果只有canBuy去分，有可能buy->cool->buy->cool.....
class Solution:
    def maxProfit(self, prices: List[int]) -> int:      
        #buy->sell/cool   (not buy)
        #cool-> buy/cool  (canBuy)
        #sell->cool
        dp={}
        def dfs(i, canBuy):
            if i>=len(prices):return 0
            
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]

            if canBuy:
                buy = dfs(i+1, False) - prices[i]
                cool = dfs(i+1, True)
                dp[(i, canBuy)] = max(buy, cool)
            else:
                sell = dfs(i+2, True)+prices[i]
                cool = dfs(i+1, False)
                dp[(i, canBuy)] = max(sell, cool)
            return dp[(i, canBuy)]
    
        return dfs(0,True)
