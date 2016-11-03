""" 
First decorator example: a decorator that endows a given function (of
one variable) with a cache.  A very good example with which we achieve
the goal of eliminating code and computation duplication.  

You must understand the LEGB scope rule to understand the code.
"""

def caching(f):
    cache = {}
    def wrapper(x):
        try:
            return cache[x]
        except:
            cache[x] = f(x)
            return cache[x]
    return wrapper

if __name__ == '__main__':
    
    def fibo(n):
        if (n==0) or (n==1):
            return 1
        else:
            return fibo(n-1) + fibo(n-2)

    fibo = caching(fibo)

    from math import sin
    sin = caching(sin)

    for i in range(1000):
        fibo(i)
    print(fibo(1020))

    for x in range(20):
        sin(x)
    print(sin.__closure__[0].cell_contents)
