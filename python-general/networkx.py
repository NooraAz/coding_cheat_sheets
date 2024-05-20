import networkx as nx

# Convert adjacency matrix to graph
nx.convert_matrix.from_numpy_matrix(arr) # older than 3.0
nx.from_numpy_array(arr) # 3.0 and newer

# drawing with positions 
nx.draw(G, pos=nx.kamada_kawai_layout(G))

# remove node(s)
G.remove_node(n)
G.remove_nodes_from(nodes_list)

# remove lonely nodes
G.remove_nodes_from(list(nx.isolates(G)))

# remove edge(s)
G.remove_edge(u,v)
edge_list = [(u1,v1),(u2,v2)]
G.remove_edges_from(edge_list)

# remove self edges
G.remove_edges_from(list(nx.selfloop_edges(G)))

# Getting neighbors of a node
G.neighbors(n) 
# It returns an iterable object, so you can easily convert it to list 
list(G.neighbors(n))

# Changing attribute of a single node
# n is the node label
nx.set_node_attributes(G, {n:65}, 'weight')

# Getting connected components
S = [G.subgraph(c).copy() for c in nx.connected_components(G)]

# checking if there is a path between two nodes
nx.has_path(G,n1,n2)

# layouts

# showing networkx graph with plotly
pos=nx.spring_layout(G,seed=1)

edge_x = []
edge_y = []
for e1,e2 in G.edges():
    x0, y0 = pos[e1]
    x1, y1 = pos[e2]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

node_x = [pos[node][0] for node in G.nodes()]
node_y = [pos[node][1] for node in G.nodes()]
node_text = list(G.nodes())

fig = px.scatter(x=node_x, y=node_y,hover_data=[node_text])
fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode='lines',line=dict(width=0.5)))
fig.update_layout(template='simple_white')
fig.show()
