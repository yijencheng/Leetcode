class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        found = [None]
        # recurive check if [p,q] can be found in this tree
        def dfs(root):
            if not root:return False, False
            lp, lq = dfs(root.left)
            rp, rq = dfs(root.right)
            p_found = lp or rp or root.val == p.val
            q_found = lq or rq or root.val == q.val
            if p_found and q_found and not found[0]:
                found[0] = root
            return p_found, q_found
        dfs(root)
        return found[0]