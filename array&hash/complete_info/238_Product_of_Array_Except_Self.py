#correct, but memory usage can less
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1]*len(nums), [1]*len(nums)
        
        tmp = 1
        for i in range(len(nums)):
            prefix[i] = tmp
            tmp*=nums[i]
        tmp = 1
        for i in range(len(nums)-1,-1,-1):
            postfix[i] = tmp
            tmp*=nums[i]
        return [prefix[i]*postfix[i] for i in range(len(nums))]

#better
class Solution:
def productExceptSelf(self, nums: List[int]) -> List[int]:
    prefix = [1]*len(nums)
    
    tmp = 1
    for i in range(len(nums)):
        prefix[i] = tmp
        tmp*=nums[i]
    tmp = 1
    for i in range(len(nums)-1,-1,-1):
        prefix[i] *= tmp
        tmp*=nums[i]
    return prefix