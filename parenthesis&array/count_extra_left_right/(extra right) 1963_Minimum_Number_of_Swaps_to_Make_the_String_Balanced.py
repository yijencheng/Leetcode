

Key
* 消去之後，最後一定會留下 ]]]]]][[[[[[[這種格式！

Sol
* find how many ]]]]] [[[[[ left
* find out how many swap it need {for the above pattern} >> a different question!
][ >>> min swap=1
]][[ >>> min swap=1
]]][[[ >>> min swap=2 (swp(0,5), swp(2,3))

Warning
* is a `swap` not a `change`~~ in case you may double count 

# suggested
class Solution:
    def minSwaps(self, s: str) -> int:
        l, extra_right = 0,0
        for p in s:
            if p == '[':
                l+=1
            else:
                if l>0:
                    l-=1
                else:
                    extra_right+=1
        
        return (extra_right+1)//2





other random idea 
* start from [a,b), all the intermediate will +=2 only the last element will remain the same

[]][]]][[[[] : [1, 0, "-1", 0, -1, -2, -3, -2, "-1", 0, 1, 0]
[][[]]][][[] : [1, 0,  1,   2,  1,  0,"-1", 0, "-1", 0, 1, 0]
[][[]][[]][] : [1, 0,  1,   2,  1,  0, 1,   2,  1,   0, 1, 0]

ref: https://www.youtube.com/watch?v=L7T-7NPgPW0
* 最後移動最後移動
    
#suggested 
#intuition (pass)
class Solution:
    def minSwaps(self, s: str) -> int:
        l, r = 0, len(s)-1
        s_l, s_r = 0,0 
        swap = 0
        while l<r:
            while l<len(s) and s_l>=0: # important to add out-of-bound check
                if s[l] == '[':
                    s_l+=1
                else:
                    s_l-=1
                l+=1
                
            while r >=0 and s_r>=0: # important to add out-of-bound check
                if s[r] == ']':
                    s_r+=1
                else:
                    s_r-=1
                r-=1
            
            if l>=len(s) or r <0:break #important
            swap+=1
            s_l,s_r = s_l+2,s_r+2 
        return swap
            

class Solution:
    def minSwaps(self, s: str) -> int:
        l, r = 0, len(s)-1
        s_l, s_r = 0,0 
        swap = 0
        while l<r:
            while s_l>=0:
                if s[l] == '[':
                   s_l+=1
                else:
                    s_l-=1

            while s_r>=0:
                if s[r] == '[':
                   s_r+=1
                else:
                    s_r-=1
            swap+=1
            s_l,s_r = 0,0 
            l,r = l+1, r-1
        return swap