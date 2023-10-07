#wrong
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q or p.val != q.val:return False 
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



#correct
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return (not p and not q)
        if p.val != q.val:return False 

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)