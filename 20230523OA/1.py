# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import collections
#every number occur uniq number of time
def solution(A):
    # Implement your solution here
    counter = collections.Counter(A)
    s = []
    for k in counter:
        s.append(counter[k])
    s = sorted(s)
    
    remove = 0
    upperbound = s[-1]
    for i in range(len(s)-2, -1, -1):
        cur = s[i]
        if upperbound == 0:
          remove+= cur
        elif cur < upperbound:
            upperbound = cur
        else:
            remove+=(cur-upperbound+1)
            upperbound-=1

    return remove
            
                
            
