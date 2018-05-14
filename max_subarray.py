A = [int(x) for x in input().split(', ')]
#print(A)

s = A[0]
min_left_s = 0
curr_res = A[0]

for i in range(1, len(A)):
	s += A[i]
	if s < min_left_s:
		#print('min_left_s = s')
		min_left_s = s
		curr_res = max(curr_res, A[i])
	else:
		curr_res = max(curr_res, s - min_left_s, A[i])
	#print('s = {0}, min_left_s = {1}, curr_res = {2}'.format(s, min_left_s, curr_res))

print(curr_res)