def read_graph(file):
	v_n, e_n = [int(x) for x in file.readline().split(' ')]

	e = []

	for line in file:
		edge = tuple(int(x) for x in line.strip('\n').split(' '))
		e.append(edge)

	return v_n, e_n, e

def make_adjacent(v_n, edges):
	adj = [[] for v in range(v_n + 1)]
	for e in edges:
		adj[e[0]].append(e[1])
		adj[e[1]].append(e[0])

	return adj

f = open('input.txt', 'r')

n, m, edges = read_graph(f)

f.close()

adjacent = make_adjacent(n, edges)

double_deg_array = []

for v in range(1, n+1):
	double_deg_array.append(0)
	for u in adjacent[v]:
		double_deg_array[v-1] += len(adjacent[u])

g = open('output.txt', 'w')

g.write(' '.join([str(x) for x in double_deg_array]))
print(double_deg_array)

g.close()