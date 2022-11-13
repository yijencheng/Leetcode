#idea: 左邊是負的，就把他切掉
https://www.youtube.com/watch?v=5WZl3MMT0Eg



#wrong!!!!!!
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = float(-inf)
        l=0
        cur_sum = float(-inf)
        for num in nums:
            cur_sum+=num
            largest = max(largest, cur_sum)
            if cur_sum <0:
                cur_sum = num
        return cur_sum
            
#correct
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = float(-inf)
        cur_sum = 0
        for num in nums:
            if cur_sum <0:
                cur_sum = num
            else:
                cur_sum+=num
            largest = max(largest, cur_sum)
            
        return largest
            
            