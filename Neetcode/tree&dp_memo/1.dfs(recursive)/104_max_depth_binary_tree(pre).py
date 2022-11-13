class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxD = [0]
        def dfs(root, curD):
            if not root:return 0
            if curD > maxD[0]:
                maxD[0] = curD
            dfs(root.left, curD+1)
            dfs(root.right, curD+1)
        
        dfs(root, 1)
        return maxD[0]