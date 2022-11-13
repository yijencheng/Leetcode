# correct
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:return [nums[:]] # need to copy!
        ans = []
        for i, num in enumerate(nums):
            remain = nums[:i]+nums[i+1: len(nums)]
            permus = self.permute(remain)
            
            for p in permus:
                ans.append([num]+p)
        return ans
                

#wrong!
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 1:return [nums[:]]
        for num in nums:
            opt = nums.pop(0)
            permus = self.permute(nums)
            
            for p in permus:
                p.append(opt)

            nums.append(opt)
        ans.extend(nums)
        return ans


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 1:return [nums[:]] #端點(leaf) logic
        for num in nums:
            opt = nums.pop(0)
            permus = self.permute(nums)
            
            for p in permus:
                p.append(opt)

            ans+=permus
            nums.append(opt)
        
        return ans
                