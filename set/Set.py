"""
Version 2: Factoring *intersection* into the superclass Set

To do this, we use a method *add* and a factory method *new* in each concreate subclass.

*intersection* is an excellent example of a template method which
describe the logic of an algorithm while delegating details of how
things work, e.g., *new* and *add* to subclasses.

*s.add(x)* is an example of a down call, which calls *add* in a subclass.
Note that *add* is not and need not be defined in *Set* 

"""

class Set:
        def intersection(self, other):
                s = self.new()
                for x in self.rep:
                        if x in other.rep:
                                s.add(x)
                return s

class DictSet(Set):
        def __init__(self,elements=()):
                rep = self.rep= {}
                for element in elements:
                        rep[element] = element

        def new(self):
                return DictSet()
                        
        def add(self, x):
                self.rep[x] = x

class ListSet(Set):
        def __init__(self,elements=()):
                rep = self.rep = []
                for element in elements:
                        if element not in rep:
                                rep.append(element)
        def new(self):
                return ListSet()

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
        
