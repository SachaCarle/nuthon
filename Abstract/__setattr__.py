self, key, value = args
if key.startswith('__') and key.endswith('__'): return object.__setattr__(self, key, value)
self.__setx__(key, value)
