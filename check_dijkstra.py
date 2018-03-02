import networkx as nx
from dijkstra import read_graph

f = open('input.txt', 'r')

n, m, edges = read_graph(f)

f.close()

G = nx.DiGraph()
G.add_weighted_edges_from(edges)
dij_dict = nx.single_source_dijkstra_path_length(G = G, source = 1)

res = [str(dij_dict.get(i, -1)) for i in range(1, n + 1)]
g = open("right_dijkstra_output.txt", 'w')
g.write(' '.join(res))
g.close()

my_output = open('output.txt', 'r')

my_res = my_output.readline().split(' ')
print(res == my_res)

my_output.close()