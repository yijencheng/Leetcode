
# correct
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        level= 0
        ans = []
        def dfs(level,root):
            if not root:return
            if len(ans) == level:
                ans.append([])
            ans[level].append(root.val)
            dfs(level+1, root.left)
            dfs(level+1, root.right)

        dfs(level, root)
        return ans



#missing level information
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        ans = []
        def dfs(root):
            if not root:return
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ans

# wrong!!! 
[1,2,3,4,5]
output: [[1],[2,3]]
expect: [[1],[2,3],[4,5]]
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        ans = [[]]
        
        def traverse(level, root):
            if not root: return
            
            if len(ans) < level+1: #first encounter this level
                ans.append([root.val])
            else:
                ans[level].append(root.val)
                traverse(level+1, root.left)
                traverse(level+1, root.right)
        
        traverse(0, root)
        return ans


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        ans = [[]]
        
        def traverse(level, root):
            if not root: return
            
            if len(ans) < level+1: #first encounter this level
                ans.append([root.val])
            else:
                ans[level].append(root.val)
            traverse(level+1, root.left)
            traverse(level+1, root.right)
        
        traverse(0, root)
        return ans


