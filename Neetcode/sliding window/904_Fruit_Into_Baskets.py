class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = {}
        l = 0
        ans = 0
        for r in range(len(fruits)):
            ## window start
            window[fruits[r]] = window.get(fruits[r], 0)+1
            while len(window.keys()) >= 3:
                window[fruits[l]] -=1
                if window[fruits[l]] == 0:
                    del window[fruits[l]]
                l+=1
            ## window end
            ans = max(ans, r-l+1)
        return ans
                 
        