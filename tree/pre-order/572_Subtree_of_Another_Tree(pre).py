#correct
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False

        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False

# still wrong. cause  when root.val == subRoot.val, it will recur down and omit cases
Ex.  [1,1] [1]
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot :return True
        if not root or not subRoot:return False

        if root.val == subRoot.val: #will escape left child possibility
            return self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# fail, even subTree not completely match, will still return True
# fail case: [3,4,5,1,2,null,null,null,null,0]  , [4,1,2] 
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:return True
        if not root:return False

        if root.val == subRoot.val:
            return self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            