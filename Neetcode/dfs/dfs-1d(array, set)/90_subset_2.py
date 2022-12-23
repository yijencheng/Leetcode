2022.11.13
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        counter = Counter(nums)
        ans = []
        def dfs(cur,idx):
            if idx == len(nums):
                ans.append(cur)
                return
            newCh, freq = nums[idx], counter[nums[idx]]
            for i in range(freq+1):
                dfs(cur.copy(), idx+freq) 
                cur+=[newCh]
        
        dfs([],0)
        return ans


====================== harder approach
[1,1,1,3, ....]
[1,1,1] + dfs([3, ....])
[1,1] + dfs([3, ...])
[1] + dfs([3, ...])

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        ans = []
        def dfs(cur, i):
            if i == len(nums):
                ans.append(cur)
                return 
            firstAppear = nums[i]
            dfs(cur+[firstAppear], i+1)
            while i<len(nums) and nums[i] == firstAppear:
                i+=1
            dfs(cur, i)
        
        dfs([], 0)
        return ans


#optimize: use global var to record `cur`
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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



#wrong
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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