self, key = args
if key == '__weakref__': return not (self.__weakref__ is None)
elif key == '__core__': return not (self.__core__ is None)
elif hasattr(self.__class__, '__in__'): return self.__in__(key)
else:
    try:
        return key in iter(self.__core__)
    except TypeError:
        assert callable(self.__core__)
        return key in self.__core__()