from dfs import DFSTimeCounter, UndirectedGraph


def find_all_nodes_in_cycle(g:UndirectedGraph): # g is an UndirectedGraph class
    set_of_nodes = set()
    dfs_tree_parents, dfs_back_edges, _, _ = g.dfs_traverse_graph()
    print("dfs_tree_parents", dfs_tree_parents)
    print("dfs_back_edges", dfs_back_edges)

    non_trivial_back_edges = [(i,j) for (i,j) in dfs_back_edges if dfs_tree_parents[i] != j]
    print("non_trivial_back_edges", non_trivial_back_edges)

    for (i, j) in non_trivial_back_edges:
        set_of_nodes.add(i)
        set_of_nodes.add(j)
        set_of_nodes.add(dfs_tree_parents[i])
        set_of_nodes.add(dfs_tree_parents[j])
    
    return set(filter(lambda x: x is not None,set_of_nodes))

#this is the example that we had for the problem.
g3 = UndirectedGraph(8)
g3.add_edge(0,1)
g3.add_edge(0,2)
g3.add_edge(0,4)
g3.add_edge(2,3)
g3.add_edge(2,4)
g3.add_edge(3,4)
g3.add_edge(5,6)
g3.add_edge(5,7)

s = find_all_nodes_in_cycle(g3)
print(f'Your code returns set of nodes: {s}')
assert s == {0,2,3,4}, 'Fail: Set of nodes must be {0,2,3,4}.'

# let's also add the edge 6,7
g3.add_edge(6,7)
s1 = find_all_nodes_in_cycle(g3)
print(f'Your code returns set of nodes: {s1}')
assert s1 == {0,2,3,4,5,6,7}, 'Fail: Set of nodes must be {0,2,3,4,5,6,7}.'

print('All tests passedd: 10 points!')