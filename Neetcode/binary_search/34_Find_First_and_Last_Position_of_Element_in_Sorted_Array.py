# wrong
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] >= target:
                r = mid-1
            else:
                l = mid+1
        
        if l == len(nums) or (l == 0 and nums[l] != target): # can also be not found in the middle
            return [-1,-1]
        
        end = l
        while end < len(nums) and nums[end] == target:
            end+=1

        return [l, end-1]

# correct
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] >= target:
                r = mid-1
            else:
                l = mid+1
        
        if l == len(nums) or (l < len(nums) and nums[l] != target):
            return [-1,-1]
        
        end = l
        while end < len(nums) and nums[end] == target:
            end+=1
            
                
        return [l, end-1]