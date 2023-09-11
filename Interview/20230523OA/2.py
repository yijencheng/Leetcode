

def solution(blocks):
    ans = 0
    # Implement your solution here
    i=0
    for i in range(len(blocks)):
        h = blocks[i]
        if (i<len(blocks)-1 and blocks[i+1]<h) or (i>=0 and blocks[i-1]<h):
            continue
        l,r = i,i
        # find leftmost number, where blocks[l-1] >= blocks [l]
        while l>0:
            if blocks[l-1]< blocks[l]:
                break
            l-=1
        while r<len(blocks)-1:
            if blocks[r+1]<blocks[r-1]:
                break
            r+=1
        ans = max(ans, r-l+1)
    return ans
        
        
