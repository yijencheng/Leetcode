#correct
# - return the index of the "1st" item larger than current


最後停的位置：
* [end, start] = [小於target的最大位置, 大於target的第一個位置]

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start,end = 0, len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if target<nums[mid]:
                end = mid-1
            elif nums[mid]<target:
                start = mid+1
            else:
                return mid
        return end+1