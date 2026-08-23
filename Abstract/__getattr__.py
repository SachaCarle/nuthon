self, key = args
if key == '__weakref__': return self.__getattribute__(key)
if key == '__core__': return self.__getattribute__(key)
return self.__getx__(key)