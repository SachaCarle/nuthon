self, *args = args
super(type(self)).__init__(type(self))
self.__core__ = None
print ("Abstract/__init__.py")