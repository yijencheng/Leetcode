# exactly the same as twoSum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,num in enumerate(nums):
            match = target-num
            if match in d:
                return [d[match], i]
            d[num] = i
