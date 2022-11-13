#better solution
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        balance = [True]

        def dfs(root):
            if not root:return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left-right) >1:
                balance[0] = False
            return max(left,right) + 1
        
        dfs(root)
        return balance[0]

#correct (top down), but can be slow
# O(n^2)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def findHeight(root):
            if not root:return 0
            return max(findHeight(root.left), findHeight(root.right))+1
        
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(findHeight(root.left)-findHeight(root.right)) <=1


#bottom-up: