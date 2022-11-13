#prerequiste: 102_binary_tree_level_order_traverse

#understanding
adjList = [[2,4],[1,3],[2,4],[1,3]]
>>> first node adList[0] has neighbor [2,4], second node adjList[1] has neighbor [2.4]...

# We push a node in the queue and make sure that the node is already cloned. Then we process neighbors. 
# If a neighbor is already cloned and visited, we just append it to the current clone neighbors list, 
# otherwise, we clone it first and append it to the queue to make sure that we can visit it in the next tick.

Time: O(V + E) - for BFS
Space: O(V) - for the hashmap



#wrong >> every node val has to be copy!
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        return Node(node.val, node.neighbors)


#wrong: infinite loop!
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        q = deque([node])
        clones = {}
        while q:
            cur = q.popleft() 
            clones[cur.val] = clones.get(cur.val, Node(cur.val, []))

            for ngbr in cur.neighbors:
                clone_ngbr = clones.get(ngbr.val, Node(ngbr.val, []))
                clones[cur.val].neighbors.append(clone_ngbr)

                q.append(ngbr)
        return clones[node.val]

#correct
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        q = deque([node])
        clones = {}
        while q:
            cur = q.popleft() 
            clones[cur.val] = clones.get(cur.val, Node(cur.val, []))

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    q.append(ngbr)

                clones[ngbr.val] = clones.get(ngbr.val, Node(ngbr.val, []))                
                clones[cur.val].neighbors.append(clones[ngbr.val])
                
        return clones[node.val]


#correct >> better!
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft() 
            cur_clone = clones[cur.val]            

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                    
                cur_clone.neighbors.append(clones[ngbr.val])
                
        return clones[node.val]