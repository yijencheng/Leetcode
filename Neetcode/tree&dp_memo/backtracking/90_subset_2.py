#wrong
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:return []
        
        ans = []
        trace = []
        def dfs(i):
            if i == len(nums):
                ans.append(trace.copy())
                return 
            #include 
            firstAppear = nums[i]
            trace.append(firstAppear)
            while i<len(nums) and nums[i] == firstAppear:
                i+=1
            dfs(i)
            
            #don't include
            trace.pop()
            dfs(i)
        
        dfs(0)
        return ans

#correct
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:return []
        nums = sorted(nums)
        
        ans = []
        trace = []
        def dfs(i):
            if i == len(nums):
                ans.append(trace.copy())
                return 
            #include 
            firstAppear = nums[i]
            trace.append(firstAppear)
            dfs(i+1)
            
            #don't include
            trace.pop()
            while i<len(nums) and nums[i] == firstAppear:
                i+=1
            dfs(i)
        
        dfs(0)
        return ans
