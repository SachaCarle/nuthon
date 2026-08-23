self, key = args
if key == '__weakref__': return object.__delattr__(self, key)
return self.__delx__(key)