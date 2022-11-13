         9 
    6          -3
   x  x    -6       2
         x    x   2     x 
                -6 -6
              -6
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = [root.val] # >> remember to set [root.val] not [0]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]

#can be correct, but TLE
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:return float('-inf')
        return max(self.maxPathSum(root.left), self.maxSumIncludeRoot(root), self.maxPathSum(root.right))

    def maxSumIncludeRoot(self, root):
        if not root:return 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            leftMax = max(left, 0)
            rightMax = max(right, 0)
            return root.val+max(leftMax, rightMax)

        left = dfs(root.left)
        leftMax = max(left, 0)
        right = dfs(root.right)
        rightMax = max(right, 0)
        return root.val+leftMax+rightMax

#wrong, because max path don't necessary need to pass through leaf
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:return float('-inf')
        return max(self.maxPathSum(root.left), self.maxSumIncludeRoot(root), self.maxPathSum(root.right))

    def maxSumIncludeRoot(self, root):
        if not root:return 0

        greatest = [float('-inf')]
        def dfs(root, cur):
            if not root:
                greatest[0] = max(greatest[0], cur)
                return 0
            cur += root.val
            dfs(root.left, cur)
            dfs(root.right, cur)
            return greatest[0]

        left = dfs(root.left, 0)
        greatest[0] = float('-inf')
        right = dfs(root.right, 0)
        return left+right+root.val