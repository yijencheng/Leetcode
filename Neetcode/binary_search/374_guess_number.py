#correct
class Solution:
    def guessNumber(self, n: int) -> int:
        start,end = 1,n
        while start<=end:
            ans = (start+end)//2
            result = guess(ans)
            if result == -1:
                end = ans-1
            elif result == 1:
                start = ans+1
            else:
                return ans
        return -1