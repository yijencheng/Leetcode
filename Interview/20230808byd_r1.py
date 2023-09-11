# input = "22512236234"
# output: how many possibility of split into ipv4 address
# * ["225.122.36.234"], ["225.12.236.234"]...
# 注意事項：
# 1. 這需要傳入i, 不需要帶整個剩下的選項

def findIPV4(s):
    ans = []
    def dfs(depth, i, cur):
        if depth == 4:
            if i == len(s):
                ans.append(cur)
            return 
        for end in range(i, i+3): #important
            tmp = s[i:end+1]
            dfs(depth+1, end+1, cur+tmp+".")
    dfs(0,0,"")
    return ans

print(findIPV4("22512236234"))
        