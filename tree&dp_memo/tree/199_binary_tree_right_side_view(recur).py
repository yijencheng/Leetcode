#wrong!!!
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        
        if root.right:
            return [root.val]+self.rightSideView(root.right)
        else:
            return [root.val]+self.rightSideView(root.left)

#wrong
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        
        rsv,lsv = [],[]
        if root.right:
            rsv =  [root.val]+self.rightSideView(root.right)
        else:
            lsv =  [root.val]+self.rightSideView(root.left)
        return rsv + lsv[len(rsv):]

#wrong!
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        
        rsv,lsv = [],[]
        if root.right:
            rsv =  self.rightSideView(root.right)
        else:
            lsv =  self.rightSideView(root.left)
        return [root.val] + rsv + lsv[len(rsv):]


#correct
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        
        rsv =  self.rightSideView(root.right)
        lsv =  self.rightSideView(root.left)
        
        return [root.val] + rsv + lsv[len(rsv):]