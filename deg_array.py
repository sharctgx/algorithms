f = open('input.txt', 'r')

v_n, e_n = [int(x) for x in f.readline().split(' ')]

e = []

for line in f:
	edge = tuple(int(x) for x in line.strip('\n').split(' '))
	e.append(edge)

print(v_n, e_n)
print(e)

f.close()

deg_array = []

for v in range(v_n):
	deg_array.append(0)
	for edge in e:
		if v+1 in edge:
			deg_array[v] += 1

g = open('output.txt', 'w')

g.write(' '.join([str(x) for x in deg_array]))
print(deg_array)
g.close()