# 為什麼會對？
>>> 因為先左再右，右同level的會把左邊的覆蓋掉、沒有同level則會留下
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        
        ans = []
        def bfs(level, root):
            if not root:return
            if len(ans) == level:
                ans.append(root.val)
            else:
                ans[level] = root.val
            bfs(level+1, root.left)
            bfs(level+1, root.right)

        bfs(0, root)
        return ans