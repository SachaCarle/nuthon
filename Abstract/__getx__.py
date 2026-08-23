#@abstractmethod from abc
self, key = args
if isinstance(key, str): return self.__getattribute__(key)
elif isinstance(key, int): return self.__core__[key]
else: raise NotImplementedError(self, '__getx__', type(key), key)