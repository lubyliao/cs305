"""

Assume that we provide two implmentation of a Set data type
because one is more efficient in certain situations than the other.

The 2 implementations use a dict and a list respectively to represent a set.

You can expect the two implementations to have very similar code, for example, 
in their implementation of union and intersection.

We would like to reduce code duplication as much as possible.

"""

class DictSet:
	def __init__(self,elements=()):
		rep = self.rep= {}
		for element in elements:
			rep[element] = element
			
	def intersection(self, other):
		rep = {}
		for x in self.rep:
			if x in other.rep:
				rep[x] = x
		s = DictSet()
		s.rep = rep
		return s

class ListSet:
	def __init__(self,elements=()):
		rep = self.rep = []
		for element in elements:
			if element not in rep:
				rep.append(element)

	def intersection(self, other):
		rep = []
		for x in self.rep:
			if x in other.rep:
				rep.append(x)
		s = ListSet()
		s.rep = rep
		return s

s = DictSet([1,2,3,4])
t = DictSet([3,4,5,6])
r = s.intersection(t)
print(r.rep)
u = ListSet([1,2,3,4])
v = ListSet([3,4,5,6])
w = u.intersection(v)
print(w.rep)
	
