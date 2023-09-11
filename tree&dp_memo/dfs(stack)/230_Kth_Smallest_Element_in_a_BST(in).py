class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        ans = []
        cur = root
        while stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            mid = stack.pop()
            ans.append(mid)
            if len(ans) == k:
                return ans[-1].val
            cur = mid.right
            
        return ans[-1]
            