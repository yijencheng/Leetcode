# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    if len(set(S)) == len(S):
        return 1
    s = set()
    split=1
    for num in S:
        if num not in s:
            s.add(num)
        else:
            split+=1
            s = set(num)
    return split
