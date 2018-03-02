class ArrayPQ:

	def __init__(self, dist):
		self._dist = dist[:]

	def delete_min(self):
		try:
			min_elem = min(i for i in self._dist if i >= 0)
			min_i = self._dist.index(min_elem)
			self._dist[min_i] = -2
		except ValueError:
			min_i = None
		return min_i

	def __getitem__(self, key):
		return self._dist[key]

	def __setitem__(self, key, value):
		self._dist[key] = value

	def __str__(self):
		return 'ArrayPQ(' + ' '.join([str(i) for i in self._dist]) + ')'

	def __repr__(self):
		return 'ArrayPQ(' + ' '.join([str(i) for i in self._dist]) + ')'