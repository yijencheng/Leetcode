Input: nums = [2,7,11,15], target = 9
Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,num in enumerate(nums):
            match = target-num
            if match in d:
                return [d[match], i]
            d[num] = i



# wrong, 
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d = {}
#         for i,num in enumerate(nums):
#             match = target-num
#             if d.get(match): #<<<<<
#                 return [d[match], i]
#             d[num] = i
