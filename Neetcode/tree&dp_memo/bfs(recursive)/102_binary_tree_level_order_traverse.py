output: [[1], [2,3], [4,5,6]]
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        if not root:return []
        q = [root]
        ans = []
        while q:
            level = []
            for i in range(len(q)):
                cur = q.pop(0)
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans.append(level)
                
        return ans



#wrong!
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        q = deque(root)
        ans = []

        while q:
            tmp = []
            for i in range(len(q)): #how many times/ # of node does this level has
                cur = q.pop()
                tmp.append(cur)
            ans.append(tmp)
        return ans

#still wrong!
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        q = deque([root])
        ans = []

        while q:
            tmp = []
            for i in range(len(q)): #how many times/ # of node does this level has
                cur = q.pop()
                tmp.append(cur.val)
                if cur.left:q.append(cur.left)
                if cur.right:q.append(cur.right)
                                     
            ans.append(tmp)
        return ans

