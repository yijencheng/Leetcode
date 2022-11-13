class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        
        ans = []
        q = [root]
        level = 0
        while q:
            for i in range(len(q)):
                cur = q.pop(0)
                if len(ans) == level:
                    ans.append([])
                ans[level] = cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            level+=1
        return ans