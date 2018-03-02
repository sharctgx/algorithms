def bubble_up(heap, new_elem):
	heap.append(new_elem)
	child = len(heap) - 1
	while (child > 0):
		parent = (child + 1) // 2 - 1
		if heap[parent] < new_elem:
			heap[parent], heap[child] = heap[child], heap[parent]
			child = parent
		else:
			break
	return heap


def build_heap(array, len_array):
	new_heap = [array[0]]
	for i in range(1, len_array):
		bubble_up(new_heap, array[i])
	return new_heap


f = open('input.txt', 'r')


n = int(f.readline())
array = [int(x) for x in f.readline().split(' ')]

heap = build_heap(array, n)

f.close()
with open ('output.txt', 'w') as g:
	g.write(' '.join([str(x) for x in heap]))