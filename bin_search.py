n = input()
m = input()
A = [int(x) for x in input().split(' ')]
values = [int(x) for x in input().split(' ')]

results = []

def do_bin_search(value, array, counter=0):
	'''Searches a value in an array, returns position in an array or -1.'''
	# print(value, array, counter)

	l = len(array)

	if l == 1:
		if array[0] == v:
			# print('found on place: {}'.format(counter))
			return counter + 1
		else:
			# print('no such elem((')
			return -1
	else:
		if array[l//2] > value:
			return do_bin_search(value, array[: l//2], counter=counter)
		else:
			return do_bin_search(value, array[l//2 :], counter=counter + l//2)


for v in values:
	results.append((do_bin_search(value=v, array=A)))

f = open('output.txt', 'w')

f.write(' '.join([str(x) for x in results]))

f.close()