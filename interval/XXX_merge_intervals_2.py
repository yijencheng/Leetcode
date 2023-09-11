#wrong, start value can be unsorted
# input: [[2,3], [4,5], [1,10]]
# output: [[2,6, a], [4,5, b], [1,10, c], expected: 
{
    1:c
    2:[a,c]
    3:[a,c]
    4:[a,b,c]
    5:[a,b,c]
    6:[a,c]
    7:[c]
    8:[c]
    9:[c]
    10:[c]
}

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