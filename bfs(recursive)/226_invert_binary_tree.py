class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:return root
        
        q = [root]
        while q:
            # for all node in this level, swap its child
            for i in range(len(q)):
                cur = q.pop(0)
                if cur.left:q.append(cur.left)
                if cur.right:q.append(cur.right)

                tmp = cur.left
                cur.left = cur.right
                cur.right = tmp
        return root