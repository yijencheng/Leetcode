# TLE, without sliding window
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        longest = 1
        for i in range(len(nums)):
            ptr = i
            total = 0
            while ptr>=0:
                total+=(nums[ptr])
                if not {condition match}:
                    break
                longest = max(longest, i-ptr+1)
                ptr-=1
        return longest

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        longest = 1
        for i in range(len(nums)):
            ptr = i
            total = nums[i]
            while ptr>=0 and (nums[i]* (i-ptr+1) - total<= k):
                longest = max(longest, i-ptr+1)
                ptr-=1
                total+=nums[ptr]
        return longest
            

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        longest = 1
        l = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            while !condition:
                total-=nums[l]
                l+=1
            longest = max(longest, i-l+1)
        return longest





ptr = i
var1 = ... 
while ptr>=0:
    ## part 1
    ## ....
    if !condition:
        break
    ## part 2
    ## ....
    ptr-=1
    


while 符合條件:
    i++