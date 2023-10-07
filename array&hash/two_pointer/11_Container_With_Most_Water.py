# optiomal substructure：if there is a better solution, than it should be contained in [start+1, end] (if height[start] < height[end])
>> 反證：  if exist better solution, it need to contain start, but then the width can only be smaller

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        start, end = 0, len(height)-1
        while start<end:
            ans = max(ans, min(height[start], height[end])*(end-start))
            if height[start]<=height[end]:
                start+=1
            else:
                end-=1
        return ans
