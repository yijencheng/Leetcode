#wrong
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        length = len(intervals)
        start = -1
        i,j = 0, length-1
        while i<=j:
            m=(i+j)//2
            cur = intervals[m]
            
            if newInterval[0] > cur[1]: #have a hard time deciding > or >=....
                j=m-1
            elif newInterval[0] <= cur[1]:
                i=m+1

#
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        length = len(intervals)
        start = -1
        i,j = 0, length-1
        while i<=j:
            m=(i+j)//2
            target = intervals[m][1]
            cur = newInterval[0]
            
            if cur <= target:
                i=m+1
            elif cur > target:
                j=m-1
