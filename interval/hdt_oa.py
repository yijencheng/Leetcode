# Imagine that there are several lamps placed on a number line, each of which illuminates some segment of the line. Specifically, the lamps are represented in a two-dimensional array lamps, where the ith lamp covers the segment from lamps[i][0] to lamps[i][1], inclusive.

# Additionally, you are given a list of control points on this number line, represented by an array points. Your task is to find the number of lamps that illuminate each control point. Specifically, for each control point points[j] in the array, your task is to find the number of lamps lamps[i] which include this point within its covered segment - when points[j] lies inside the segment [lamps[i][0], lamps[i][1]].

# As a result, return an array of integers, where ith integer corresponds to the answer for the ith control point.

# Example

# For lamps = [[1, 7], [5, 11], [7, 9]] and points = [7, 1, 5, 10, 9, 15], the output should be solution(lamps, points) = [3, 1, 2, 1, 2, 0].

def solution(lamps, points):
    lamps.sort(key=lambda x: x[0])
    
    start,end = [], []
    for l in lamps:
        start.append(l[0])
        end.append(l[1])
    end.sort()
    
    d = {} # record point's ans
    ptr1,ptr2 = 0,0
    cur = 0
    for i in range(max(points)+1):
        # meet start
        while ptr1 < len(start) and i == start[ptr1]:
            cur+=1
            ptr1+=1
        d[i] = cur
        # meet end
        while ptr2 < len(end) and i == end[ptr2]:
            cur-=1
            ptr2+=1
        
        # if ptr1 == len(start) and ptr2 == len(end):
        #     break
    
    ans = []
    for p in points:
        ans.append(d[p])
    return ans
        
        

