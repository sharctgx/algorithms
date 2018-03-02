from queue import Queue

def read_graph(file):
	v_n, e_n = [int(x) for x in file.readline().split(' ')]

	e = []

	for line in file:
		edge = tuple(int(x) for x in line.strip('\n').split(' '))
		e.append(edge)

	return v_n, e_n, e

def make_adjacent(v_n, edges, oriented = False):
	adj = [[] for v in range(v_n + 1)]
	if oriented:
		for e in edges:
			adj[e[0]].append(e[1])
	else:
		for e in edges:
			adj[e[0]].append(e[1])
			adj[e[1]].append(e[0])

	return adj

def bfs(v_n, adjacent):
	'''Distances to other vertices from vertice 1.
	'''
	dist = [-1]*(v_n+1)
	dist[1] = 0

	Q = Queue(maxsize = 0)
	Q.put_nowait(1)
	while (Q.empty() != True):
		u = Q.get_nowait()
		for u_friend in adjacent[u]:
			if dist[u_friend] == -1:
				Q.put_nowait(u_friend)
				dist[u_friend] = dist[u] + 1

	return dist


f = open('input.txt', 'r')

n, m, edges = read_graph(f)

f.close()

adjacent = make_adjacent(n, edges, oriented = True)
distances = bfs(n, adjacent)
print(adjacent)

g = open('output.txt', 'w')

g.write(' '.join([str(x) for x in distances[1:]]))
print(distances[1:])

g.close()