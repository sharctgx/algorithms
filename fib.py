def fib(n):
	if n==0:
		return 0
	if n==1:
		return 1
	else:
		f1 = 0
		f2 = 1
		for i in range(2, n+1):
			res = f2 + f1
			f1 = f2
			f2 = res
		return res

f = open('fib.txt', 'r')
result = fib(int(f.read()))
f.close()

g = open('output.txt', 'w')
g.write(str(result))
g.close()