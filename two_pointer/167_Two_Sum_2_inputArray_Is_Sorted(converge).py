Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

#correct
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start,end = 0, len(numbers)-1
        while start != end:
            cur = numbers[start]+numbers[end]
            if cur>target:
                end-=1
            elif cur<target:
                start+=1
            else:
                return [start+1,end+1]
        return None