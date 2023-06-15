import networkx as nx

# convert adjacency matrix to graph
nx.convert_matrix.from_numpy_matrix(arr)

# drawing with positions 
nx.draw(G, pos=nx.kamada_kawai_layout(G))

# remove a node
G.remove_node(n)

# remove edges in an edge list
edge_list = [(u1,v1),(u2,v2)]
G.remove_edges_from(edge_list)

# getting neighbors of a node
G.neighbors(n) 
# it returns an iterable object, so you can easily convert it to list 
list(G.neighbors(n))

# changing attribute of a single node
# n is node label
nx.set_node_attributes(G, {n:65}, 'weight')

# getting connected components
S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
