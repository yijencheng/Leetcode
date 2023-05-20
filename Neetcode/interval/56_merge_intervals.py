#wrong, start value can be unsorted
# input: [[2,3], [4,5], [1,10]]
# output: [[2,3], [4,5], [1,10]], expected: [[1,10]]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        tmp = None
        ans = []
        for interval in intervals:
            if not tmp:
                tmp = interval
                continue
            elif tmp[1]<interval[0]:
                ans.append(tmp)
                tmp = interval
            elif interval[1]<tmp[0]:
                ans.append(interval)
            else:
                tmp[0],tmp[1] = min(interval[0],tmp[0]), max(interval[1], tmp[1])
        ans.append(tmp)
        return ans


# correct
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        tmp = None
        ans = []
        
        intervals.sort(key=lambda x: x[0]) #should be put in the front
        for interval in intervals:
            if not tmp:
                tmp = interval
                continue
            elif tmp[1]<interval[0]:
                ans.append(tmp)
                tmp = interval
            elif interval[1]<tmp[0]:
                ans.append(interval)
            else:
                tmp[0],tmp[1] = min(interval[0],tmp[0]), max(interval[1], tmp[1])
        ans.append(tmp)
        return ans


# refactor step1
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        tmp = intervals[0] # redundant
        ans = []
        for interval in intervals[1:]:
            if tmp[1]<interval[0]: #less than
                ans.append(tmp)
                tmp = interval
            elif interval[1]<tmp[0]: #larger than  >>>> will not happen!!
                ans.append(interval)
            else: #merge
                tmp[0],tmp[1] = min(interval[0],tmp[0]), max(interval[1], tmp[1])
        ans.append(tmp)
        return ans 


# refactor step2
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        ans = [intervals[0]]
        for canidate in intervals[1:]:
            last = ans[-1]
            if last[1]<canidate[0]:
                ans.append(canidate)
            else: #merge
                ans[-1] = min(canidate[0],last[0]), max(canidate[1], last[1])
        return ans