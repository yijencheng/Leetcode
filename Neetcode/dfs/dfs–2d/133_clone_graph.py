#correct
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        clones = {
            node.val:Node(node.val)
        }
        def dfs(root):
            for ngbr in root.neighbors:
                if ngbr.val not in clones:        
                    clones[ngbr.val] = Node(ngbr.val)
                    dfs(ngbr)
                clones[root.val].neighbors.append(clones[ngbr.val])
            return
                
        dfs(node)
        return clones[node.val]

#wrong!
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        clones = {
            node.val:Node(node.val)
        }
        def dfs(root):
            for ngbr in root.neighbors:
                if ngbr.val not in clones:        
                    clones[ngbr.val] = Node(ngbr.val)
                    clones[root.val].neighbors.append(clones[ngbr.val])
                    dfs(clones[ngbr.val])
            return root
                
                
        return dfs(node)


#wrong
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        clones = {
            node.val:Node(node.val)
        }
        def dfs(root):
            for ngbr in root.neighbors:
                if ngbr.val not in clones:        
                    clones[ngbr.val] = Node(ngbr.val)
                    clones[root.val].neighbors.append(clones[ngbr.val])
                    dfs(ngbr)
            return
                
        dfs(node)
        return clones[node.val]
