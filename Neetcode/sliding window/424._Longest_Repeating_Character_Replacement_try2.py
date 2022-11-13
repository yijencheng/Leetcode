Input: s = "ABAB", k = 2
Output: 4



#wrong
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #use the 1st as target(標準)
        l = 0
        longest = 0
        for r in range(1, len(s)):
            old = s[l]
            if k == 0:
                while s[l] == old:
                    k+=1
                    l+=1
            longest = max(longest, r-l+1)
            k-=1
                
        return longest

#wrong    ....
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #use the 1st as target(標準)
        l = 0
        longest = 0
        for r in range(1, len(s)):
            old = s[l]
            if k == 0:
                while s[l] == old:
                    k+=1
                    l+=1
            longest = max(longest, r-l+1)
            if s[r] != s[l]:
                k-=1
                
        return longest


#two case
AAAAAAAABACAAAB , k=2
AAAAAAAABABAAAB , k=2
>> 當縮到第一個的時候，中間「其他數字」的數量要<=k
- 我怎麼知道其他數字有幾個？  A.中間一定是k-1個A以外的數字，其他都是Ａ
- 那我怎麼知道A以外的數字，到底跟new start一不一樣呢？
A. 你不知道 QQ 因此要用map記住
.......
太麻煩了。
更好的做法是記住 "most-frequent number"
            
                
        