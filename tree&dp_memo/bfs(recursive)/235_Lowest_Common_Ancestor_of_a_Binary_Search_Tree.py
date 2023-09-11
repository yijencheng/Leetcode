# correct
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:return root
        
        queue = [root]
        while queue:
            #current level
            for i in range(len(queue)):
                cur = queue.pop(0)
                if min(p.val, q.val) <= cur.val and cur.val <= max(p.val, q.val):
                    return cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

# found the Wrong answer!
* p, q 不一定誰大誰小
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:return root
        queue = [root]
        while queue:
            #current level
            for i in range(len(queue)):
                cur = queue.pop(0)
                if p.val < cur.val and cur.val <q.val:
                    return cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)