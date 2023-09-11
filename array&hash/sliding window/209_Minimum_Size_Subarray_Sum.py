# without sliding window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        for i in range(len(nums)):
            ptr = i
            total = nums[ptr]
            while ptr >= 0 and total < target:
                ptr-=1
                total += nums[ptr]
            if ptr!=-1:
                min_length = min(min_length, i-ptr+1)
        
        if min_length == float("inf"):return 0
        return min_length

# correct, with sliding window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        total = 0
        l = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                min_length = min(min_length, i-l+1)
                total-=nums[l]
                l+=1
        if min_length == float("inf"):
            return 0
        return min_length