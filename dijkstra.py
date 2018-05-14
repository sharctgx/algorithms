from queue import Queue
from priority_queues import ArrayPQ

def read_graph(file):
	v_n, e_n = [int(x) for x in file.readline().split(' ')]

	e = []

	for line in file:
		edge = tuple(int(x) for x in line.strip('\n').split(' '))
		e.append(edge)

	return v_n, e_n, e

def make_adjacent(v_n, edges, oriented = False, weighted = False):
	if weighted:
		adj = [dict() for v in range(v_n + 1)]
		if oriented:
			for e in edges:
				prev = adj[e[0]].get(e[1], None)
				if prev:
					if (prev <= e[2]):
						pass
					else:
						adj[e[0]][e[1]] = e[2]
				else:
					adj[e[0]][e[1]] = e[2]
		else:
			raise NotImplementedError
	else:
		adj = [[] for v in range(v_n + 1)]
		if oriented:
			for e in edges:
				adj[e[0]].append(e[1])
		else:
			for e in edges:
				adj[e[0]].append(e[1])
				adj[e[1]].append(e[0])

	return adj

def dijkstra(v_n, adjacent, logfile):
	'''Distances to other vertices from vertice 1 in weighted graph.
	'''
	dist = [-1]*(v_n + 1)
	dist[1] = 0
	Q = ArrayPQ(dist)

	log = open(logfile, 'w')

	while True:
		u = Q.delete_min()
		log.write('u = {}\n'.format(u))

		if not u:
			break

		log.write(str(adjacent[u]) + '\n')

		for nu, l in adjacent[u].items():
			log.write('nu = {}\n'.format(nu))
			log.write('comparing: {} {}\n'.format(dist[nu], (dist[u] + l)))
			if (dist[nu] == -1) | (dist[nu] > dist[u] + l):
				dist[nu] = dist[u] + l
				log.write('now dist[nu] = {}\n'.format(dist[nu]))
				Q[nu] = dist[nu]
		log.write(str(Q) + '\n')
				
	return dist


f = open('input.txt', 'r')

n, m, edges = read_graph(f)

f.close()

adjacent = make_adjacent(n, edges, oriented = True, weighted = True)
#print(adjacent)
#print(min(edges, key= lambda i : i[2]))

distances = dijkstra(n, adjacent, 'log.txt')

g = open('output.txt', 'w')

g.write(' '.join([str(x) for x in distances[1:]]))
print(distances[1:])

g.close()