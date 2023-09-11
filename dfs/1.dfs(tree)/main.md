# Template
    def solve(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def dfs(root):
            if not root:return
            # xxx
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ans[-1]