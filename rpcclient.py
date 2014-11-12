import pickle

class RPCProxy:
    def __init__(self, connection):
        self._connection = connection
    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(pickle.dumps((name, args, kwargs)))
            result = pickle.loads(self._connection.recv())
            if isinstance(result, Exception):
                raise result
            return result
        return do_rpc

# Example use
from multiprocessing.connection import Client
c = Client(('beowulf.ucsd.edu', 1234), authkey=b'peekaboo')
proxy = RPCProxy(c)
print(proxy.fibo(123))
print(proxy.add(234, 789))
print(proxy.sub(2, 3))
try:
    proxy.sub([1, 2], 4)
except Exception as e:
    print(e)
