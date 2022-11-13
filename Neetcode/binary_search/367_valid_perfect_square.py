#wrong: #input=1, output=false, expected=true
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 1, num//2
        while start<=end:
            mid = (start+end)//2
            if mid**2 < num:
                start = mid+1
            elif num < mid**2:
                end = mid-1
            else:
                return True
        return False

#correct, right bound 要是有可能答案的最右邊
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 0, num//2+1
        while start<=end:
            mid = (start+end)//2
            if mid**2 < num:
                start = mid+1
            elif num < mid**2:
                end = mid-1
            else:
                return True
        return False

