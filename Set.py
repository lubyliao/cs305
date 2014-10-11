"""
This version replaces factory method with factory function.  

"""

def new(obj, *args, **kw):      # Factory function
    return type(obj)(*args, **kw)

def iterator(s):
    for x in s.rep:
        yield x

class Set:

    def intersection(self, other): # An example of a template method
        # s = self.new()           # Used factory method in the previous version
        s = new(self)           # Use factory function instead
        for x in self:          
            if x in other:      
                s.add(x)
        return s

    def __iter__(self):
        return iterator(self)

class DictSet(Set):

    def __init__(self, elements=[]):
        rep = self.rep = {}
        for element in elements:
            rep[element] = element

    # def new(self):              # No longer needed
    #     return DictSet()

    def add(self, x):           
        self.rep[x] = x

class ListSet(Set):

    def __init__(self, elements=[]):
        rep = self.rep = []
        for element in elements:
            if element not in rep:
                rep.append(element)

    def add(self, x):
        self.rep.append(x)


s = ListSet([1,2,3,1,2,3])
r = ListSet([2,3,4])
w = s.intersection(r)
print(s.rep)
print(r.rep)
print(w.rep)
