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
                cur_sum = num ## wrong here
        return cur_sum
            
#correct
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = float(-inf)
        cur_sum = 0
        for num in nums:
            ## Also can replace with: cur_sum = max(cur_sum+num, num)
            if cur_sum <0:
                cur_sum = 0
            cur_sum+=num
            ## 
            largest = max(largest, cur_sum)
            
        return largest

# also correct. For front vs back, see how-to: cumulate
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res

# also correct~~~
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        largest = nums[0]
        for num in nums:
            cur_sum = max(cur_sum+num, num)
            largest = max(largest, cur_sum)
            
        return largest


            
            