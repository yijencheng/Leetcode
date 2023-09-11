Q. level要先加還是後加？
A. 


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0

        q = [root]
        level = 0
        while q:
            level+=1

            #pop all current level's node
            for i in range(len(q)):
                cur = q.pop(0)
                if cur.left:q.append(cur.left)
                if cur.right:q.append(cur.right)
            
        return level


#wrong！ queue should pop(0) rather than pop()
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0

        q = [root]
        level = 0
        while q:
            level+=1

            #pop all current level's node
            for i in range(len(q)):
                cur = q.pop()
                if cur.left:q.append(cur.left)
                if cur.right:q.append(cur.right)
            
        return level