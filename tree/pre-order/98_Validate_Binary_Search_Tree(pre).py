# two things to keep an eye
* 先還是後？
* 如何更新min, max

#best: use "boundary"
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            ) # why node.val is always a tighter upper bound for left child?
            # because the previous upper bound is `when node.val is the left child of others`

        return valid(root, float("-inf"), float("inf"))

5
 \
   7
  /
6


# correct. But it is too complicate 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = [True]
        l, u = float("-inf"), float("inf")
        def dfs(root,l,u):
            if not root:return
            
            if root.left and not (l< root.left.val < min(u, root.val)):
                valid[0] = False
                return
            if root.right and not (max(l, root.val)< root.right.val < u):
                valid[0] = False
                return
            dfs(root.left, l, min(u, root.val))
            dfs(root.right, max(l, root.val), u)
        
        dfs(root, l, u)
        return valid[0]

# wrong 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = [True]
        curMin, curMax = float("inf"), float("-inf")
        def dfs(root,curMin,curMax):
            if not root:return
            
            curMin = min(curMin, root.val)
            curMax = max(curMax, root.val)
            print(root.val, curMin, curMax)
            if root.left and not (root.left.val < curMin):
                valid[0] = False
                return
            if root.right and not (root.right.val > curMax):
                valid[0] = False
                return
            dfs(root.left, curMin, curMax)
            dfs(root.right, curMin, curMax)
        
        dfs(root, curMin, curMax)
        return valid[0]


#wrong
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True
        def dfs(root):
            if not root:return

            if root.left and not (root.left.val < root.val):
                valid = False
                return
            if root.right and not (root.right.val > root.val):
                valid = False
                return
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return valid