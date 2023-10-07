# correct 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:return [[]]
        ans = []
        trace = []
        def dfs(i):
            if i == len(nums):
                ans.append(trace.copy())
                return

            #if choose
            trace.append(nums[i])
            dfs(i+1)
            
            #not choose
            trace.pop()
            dfs(i+1)
        
        dfs(0)
        return ans
            

#wrong >> 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:return []
        ans = [nums]
        for _ in range(len(nums)):
            mustInclude = nums.pop(0)
            subsets = self.subsets(nums)
            for sub in subsets:
                sub.append(mustInclude)
            
            ans+=subsets
        return ans

#mine
#idea: 一定包含第一個elemt的、移除掉第一個後，一定包含第二個element的...
#the reason why here we need nums.copy() but 46_permutations does not
#is that 46. after pop & append it will remain the same, while here it will change nums array
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:return [[]]
        ans = []
        for _ in range(len(nums)):
            mustInclude = nums.pop(0)
            subsets = self.subsets(nums.copy())
            for sub in subsets:
                sub.append(mustInclude)
            ans+=subsets
        ans.append([])
        return ans


#anotehr goood sol.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:return [[]]
        ans = []
        trace = []
        def dfs(i):
            if i == len(nums):
                ans.append(trace.copy())
                return

            #if choose
            trace.append(nums[i])
            dfs(i+1)
            
            #not choose
            trace.pop()
            dfs(i+1)
        
        dfs(0)
        return ans
            