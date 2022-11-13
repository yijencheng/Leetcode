missing:
- two pointer logic
- check same 

#optimal
def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


#correct
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:continue

            target = -num
            start, end = i+1, len(nums)-1
            while start<end:
                if start > i+1 and nums[start] == nums[start-1]:
                    start+=1
                    continue

                cur =nums[start]+nums[end]
                if  cur == target:
                    ans.append([num, nums[start], nums[end]])
                    start, end = start+1, end-1
                elif cur > target:
                    end-=1
                else:
                    start +=1
        return ans
                    

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:continue

            target = -num
            start, end = i+1, len(nums)
            while start<end:
                if start > i+1 and nums[start] == nums[start-1]:continue

                if nums[start]+nums[end] == target:
                    ans.append([num, nums[start], nums[end]])
                    start, end = start+1, end-1