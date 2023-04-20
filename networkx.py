import networkx as nx

# convert adjacency matrix to graph
nx.convert_matrix.from_numpy_matrix(arr)

# drawing with positions 
nx.draw(G, pos=nx.kamada_kawai_layout(G))
