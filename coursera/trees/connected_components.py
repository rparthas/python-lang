# Find the number of (maximal) strongly connected components in an undirected graph from the results of a DFS. 
# Implement the function num_connected_components that takes in a graph g and returns a number that indicates the number of MSCCs in the directed graph.
from dfs import DFSTimeCounter, UndirectedGraph


def num_connected_components(g): # g is an UndirectedGraph class
    dfs_timer = DFSTimeCounter()
    discovery_times = [None] * g.n
    finish_times = [None] * g.n
    dfs_tree_parents = [None] * g.n
    dfs_back_edges = []
    num_components = 0
    
    for i in range(g.n):
        if discovery_times[i] is None:
            g.dfs_visit(i, dfs_timer, discovery_times, finish_times, dfs_tree_parents, dfs_back_edges)
            num_components += 1
    
    return num_components

# create the graph from problem 1A.
g = UndirectedGraph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,4)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,4)

assert num_connected_components(g) == 1, f' Test A failed: g must have 1 connected component. Your code returns {num_connected_components(g)}'


g2 = UndirectedGraph(7)
g2.add_edge(0,1)
g2.add_edge(0,2)
g2.add_edge(0,4)
g2.add_edge(2,3)
g2.add_edge(2,4)
g2.add_edge(3,4)
g2.add_edge(5,6)

assert num_connected_components(g2) == 2, f' Test B failed: g2 must have 2 connected components. Your code returns {num_connected_components(g2)}'


g3 = UndirectedGraph(8)
g3.add_edge(0,1)
g3.add_edge(0,2)
g3.add_edge(0,4)
g3.add_edge(2,3)
g3.add_edge(2,4)
g3.add_edge(3,4)
g3.add_edge(5,6)

assert num_connected_components(g3) == 3, f' Test C failed: g3 must have 3 connected components. Your code returns {num_connected_components(g3)}'

g3.add_edge(7,5)
assert num_connected_components(g3) == 2, f' Test D failed: g3 must now have 2 connected components. Your code returns {num_connected_components(g3)}'

print('All tests passed: 15 points!')