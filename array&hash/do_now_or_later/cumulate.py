Problem: [1,2,3,4]


[1, 3, 6, 10] left -> right
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cum = 0
        ans = [0]*len(nums)
        for i in range(len(nums)):
            cum+=nums[i]
            ans[i] = cum
        return ans

[0,1,3,6]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cum = 0
        ans = [0]*len(nums)
        for i in range(len(nums)):
            ans[i] = cum
            cum+=nums[i]

        return ans

