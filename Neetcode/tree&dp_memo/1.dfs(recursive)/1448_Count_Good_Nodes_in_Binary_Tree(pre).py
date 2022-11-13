#correct
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curMax = float('-inf')
        goodNode = [0]
        def dfs(curMax, root):
            if not root:return
            if curMax <= root.val:
                goodNode[0]+=1
                curMax = root.val
            dfs(curMax, root.left)
            dfs(curMax, root.right)
        
        dfs(curMax, root)
        return goodNode[0]