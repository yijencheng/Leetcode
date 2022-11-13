#wrong
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i, interval in enumerate(intervals):
            if interval[1]<newInterval[0]:continue
            elif newInterval[1]<interval[0]:
                return intervals[:i]+newInterval+intervals[i:]
            else:
                newInterval[0] = min(interval[0],newInterval[0])
                newInterval[1] = min(interval[1],newInterval[1])
            
                
#wrong
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        for i, interval in enumerate(intervals):
            if interval[1]<newInterval[0]:
                ret.append(interval)
            elif newInterval[1]<interval[0]:
                ret.append(newInterval)
                return ret + intervals[i:]
            else:
                newInterval[0] = min(interval[0],newInterval[0])
                newInterval[1] = min(interval[1],newInterval[1])
            
                
#wrong: 
# input: [[1,5]] , newInterval=[2,3], output=[]
# return 放在elif 裡面，但最後一個不一定會進去，因此newInterval有可能被忽略
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        if len(intervals) == 0:return [newInterval]

        for i, interval in enumerate(intervals):
            if interval[1]<newInterval[0]:
                ret.append(interval)
            elif newInterval[1]<interval[0]:
                ret.append(newInterval)
                return ret + intervals[i:]
            else:
                newInterval[0] = min(interval[0],newInterval[0])
                newInterval[1] = max(interval[1],newInterval[1])
            
# correct. 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        for i, interval in enumerate(intervals):
            if interval[1]<newInterval[0]:
                ret.append(interval)
            elif newInterval[1]<interval[0]:
                ret.append(newInterval)
                return ret + intervals[i:]
            else:
                newInterval[0] = min(interval[0],newInterval[0])
                newInterval[1] = max(interval[1],newInterval[1])
        ret.append(newInterval) 
        return ret
            
                
           
        
