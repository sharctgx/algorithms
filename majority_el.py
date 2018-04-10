k, n = [int(x) for x in input().split(' ')]

res = []

def find_maj_el(array):
	'''Finds majority element in an array or returns -1.
	   Has O(nlogn) complexity.
	'''

	l = len(array)

	if l == 1:
		return array[0]
	else:
		maj1 = find_maj_el(array[: l//2])
		maj2 = find_maj_el(array[l//2 :])
		if maj1 == maj2:
			return maj1
		else:
			count1 = 0
			count2 = 0
			for i in array:
				if i == maj1:
					count1 += 1
				if i == maj2:
					count2 += 1
			if (count1 >= l//2 + 1):
				return maj1
			if (count2 >= l//2 + 1):
				return maj2
			else:
				return -1


for i in range(k):
	A = [int(x) for x in input().split(' ')]
	res.append(find_maj_el(array=A))


f = open('output.txt', 'w')

f.write(' '.join([str(x) for x in res]))

f.close()