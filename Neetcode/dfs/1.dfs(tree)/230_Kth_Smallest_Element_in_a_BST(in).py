# can do this
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def dfs(root):
            if not root:return
            dfs(root.left)

            if len(ans) == k:return
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return ans[-1]

# try to optiize, but wrong because the node.val will continue be append without checking len(ans) ==k 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def dfs(root):
            if not root or len(ans) == k:return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return ans[-1]
#correct
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def dfs(root):
            if not root:return
            dfs(root.left)
            if len(ans) < k:
                ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return ans[-1]