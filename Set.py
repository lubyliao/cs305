"""

Assume that we would like to provide two implmentations of a Set data type.
The motivation is that one is more efficient than the other under different situations.

These two implementations use a dict and a list respectively to repesent a set.

You can expect the two implementations to have very similar code. 
For example, their implementation of union and intersection should be nearly identical.

We would like to reduce code duplication as much as possible.

As the code evolves, we introduced

  -- factory method pattern

  -- template method, such as Set.intersection(self, other) which
     contains the logic of finding the intersection of two sets, but
     delegates details to concrete subclasses.

  -- iterator (with generator).  This allows us to write 

       for x in self
     
     instead of "for x in self.rep", in Set.intersection

  -- factory function (see next version)

"""

def iterator(s):
    for x in s.rep:
        yield x

class Set:

    def intersection(self, other): # An example of a template method
        s = self.new()          # An example of the factory method pattern, see Wikipedia
        for x in self:          # existence of an iterator allows us to say this
            if x in other:      # and this
                s.add(x)
        return s

    def __iter__(self):
        return iterator(self)

class DictSet(Set):

    def __init__(self, elements=[]):
        rep = self.rep = {}
        for element in elements:
            rep[element] = element

    def new(self):
        return DictSet()

    def add(self, x):
        self.rep[x] = x

    # def intersection(self, other):
    #     rep = {}
    #     for x in self.rep:
    #         if x in other.rep:
    #             rep[x] = x
    #     s = DictSet()
    #     s.rep = rep
    #     return s

class ListSet(Set):

    def __init__(self, elements=[]):
        rep = self.rep = []
        for element in elements:
            if element not in rep:
                rep.append(element)

    def new(self):
        return ListSet()

    def add(self, x):
        self.rep.append(x)
    
                
    # def intersection(self, other):
    #     rep = []
    #     for x in self.rep:
    #         if x in other.rep:
    #             rep.append(x)
    #     s = ListSet()
    #     s.rep = rep
    #     return s



s = ListSet([1,2,3,1,2,3])
t = DictSet([1,2,3,1,2,3])
for x in s:
    print(x)

for x in t:
    print(x)

# r = ListSet([2,3,4])
# w = s.intersection(r)
# print(s.rep)
# print(r.rep)
# print(w.rep)
