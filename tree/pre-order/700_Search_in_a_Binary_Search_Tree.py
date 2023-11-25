class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:return None
        if root.val == val:return root

        node = None
        if val< root.val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)