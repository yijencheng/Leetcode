#correct
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def depth(root):
            if not root:return -1
            left = depth(root.left)
            right = depth(root.right)
            res[0] = max(res[0], left+right+2)
            return max(left, right)+1
        
        depth(root)
        return res[0]

#global var error
class Solution:
     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        def depth(root):
            if not root:return -1
            left = depth(root.left)
            right = depth(root.right)
            maxDepth = max(maxDepth, left+right+2)
            return max(left, right)+1
        
        depth(root)
        return maxDepth
            
# try2 – still wrong
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if not root:return -1
            return max(depth(root.left), depth(root.right))+1
        
        return depth(root.left)+depth(root.right)+2

# wrong
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if not root:return 0
            return max(depth(root.left), depth(root.right))+1
        
        return depth(root.left)+depth(root.right)+1

