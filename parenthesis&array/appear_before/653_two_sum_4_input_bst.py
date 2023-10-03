class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        def traverse(root):
            if not root:
                return
            if k-root.val in s:
                return True
            s.add(root.val)
            return traverse(root.left) or traverse(root.right)
        
        return traverse(root)