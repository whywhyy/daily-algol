# Clone Graph
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        
        new_nodes = dict()
        return self.dfs(node, new_nodes)
    
    
    def dfs(self, node, new_nodes: Dict) -> 'Node':
        # 'node' is always an 'old' node and not its copy (if it exists)
        if node.val in new_nodes:
            # node is already being cloned at upper levels of the recursion
            return new_nodes[node.val]
        
        # else this is our first encounter with the node
        new_neighbours = []
        new_node = Node(node.val, new_neighbours)
        new_nodes[node.val] = new_node
        
        for neighbour in node.neighbors:
            # recursively clone neighbour
            new_neighbour = self.dfs(neighbour, new_nodes)
            new_neighbours.append(new_neighbour)
            
        return new_node