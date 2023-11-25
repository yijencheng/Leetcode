def main():
   ans = []
   def dfs(root):
    if not root:
       return
    dfs(root.left)
    dfs(root.right)
   
   dfs(root)
main()


def dfs(i):
    if i < 0:
        return 0
    
    return  max(dfs(i-2)+nums[i], dfs(i-1)) 
return dfs(len(nums)-1)