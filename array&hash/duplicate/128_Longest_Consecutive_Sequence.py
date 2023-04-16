#success
#tips: 判斷第一個的方法，是看前面一個數字「沒有出現」
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        appear = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in appear:
                tmp = num +1
                while tmp in appear:
                    tmp+=1
                longest = max(longest, tmp-1-num+1)
        return longest