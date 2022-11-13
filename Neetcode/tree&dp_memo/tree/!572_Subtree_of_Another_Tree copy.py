#
Subtree & Sametree are not the same.

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:return True

        if not root :return False
    
        if root.val != subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            if root.left and subRoot.left and root.right and subRoot.right:
                return self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)
            if not root.left and not root.right and not subRoot.left and not subRoot.right:
                return True
            return False

# still wrong. Because [1,1] [1] cannot find 
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:return True
        if (root and not subRoot) or (not root and subRoot):return False
    
        if root.val!=subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return (self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right))

#wrong
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root and not subRoot) or (not root and subRoot):return False
        
        if root.val!=subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)