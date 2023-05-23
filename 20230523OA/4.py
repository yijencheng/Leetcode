# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    l,r = 0,0
    # sol1: delete all A
    ans1 = 0
    for num in S:
        if num == 'A':
            ans1+=1
    # sol2: keep A
    
    prefixB=0
    firstA = 0
    while firstA < len(S) and S[firstA] != 'A':
        prefixB+=1
        firstA+=1
    lastA = len(S)
    # remove all B between 1stA and lastA
    ans2 = prefixB
    for i in range(len(S)-1, firstA,-1):
        if S[i] == 'A':
            lastA = i
            break
    for i in range(firstA, lastA+1):
        if S[i] == 'B':
            ans2+=1
    # remove all A after first B
    ans3 = prefixB
    firstB = firstA+1
    while firstB < len(S) and S[firstB] == 'A':
        firstB+=1
    for num in range(firstB, len(S)):
        if S[num] == 'A':
            ans3+=1 
    return min(ans1,ans2, ans3)   