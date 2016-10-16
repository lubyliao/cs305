""" Version 3: replacing the N-factory methods with one factory function. """ 

def new(C, *args, **kw):
        return C(*args, **kw)

class Set:

        def intersection(self, other):
                s = new(type(self))
                for x in self.rep:
                        if x in other.rep:
                                s.add(x)
                return s

class DictSet(Set):
        def __init__(self,elements=()):
                rep = self.rep= {}
                for element in elements:
                        rep[element] = element

        def add(self, x):
                self.rep[x] = x

class ListSet(Set):
        def __init__(self,elements=()):
                rep = self.rep = []
                for element in elements:
                        if element not in rep:
                                rep.append(element)

        def add(self, x):
                self.rep.append(x)


s = DictSet([1,2,3,4])
t = DictSet([3,4,5,6])
r = s.intersection(t)
print(r.rep)
u = ListSet([1,2,3,4])
v = ListSet([3,4,5,6])
w = u.intersection(v)
print(w.rep)
        
