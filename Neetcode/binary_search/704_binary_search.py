#approach1: template
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j=0,len(nums)-1
        while i<=j:
            m =(i+j)//2
            if nums[m] <target:
                i=m+1
            elif nums[m] >target:
                j=m-1
            else:
                return m
        return -1


# approach2: invariate
# https://stackoverflow.com/questions/6553970/find-the-first-element-in-a-sorted-array-that-is-greater-than-the-target
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j=0,len(nums)-1
        while i<=j:
            m =(i+j)//2
            if nums[m] <=target:
                i=m+1
            elif nums[m] >target:
                j=m-1
        return j if nums[j] == target else -1:



0,1,2,3 >> 