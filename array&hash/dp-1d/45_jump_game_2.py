# more like DP
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [float('inf')]*len(nums) # steps need to take to visit point i
        res[0] = 0
        for i in range(len(nums)):
            right = min(len(nums), i+nums[i]+1) #新選項的出現，讓新的地方可以被抵達
            for j in range(i+1, right):
                res[j] = min(res[j], res[i]+1)
        return res[-1]