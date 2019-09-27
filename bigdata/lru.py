import collections

class LRUCache():

	def __init__(self, capacity):
		self.capacity = capacity
		self.cache = collections.OrderedDict()

	def get(self,key):
		if not key in self.cache:
			return -1
		value = self.cache.pop(key)
		self.cache[key] = value
		return value

	def set(self, key, value):
		if key in self.cache:
			self.cache.pop(key)
		elif len(self.cache) == self.capacity:
			self.cache.popitem(last=False)
		self.cache[key] = value

if __name__ == "__main__":
	cache = LRUCache(3)
	cache.set(1,1)
	cache.set(2,2)
	cache.set(3,3)
	print(cache.get(1))
