self, *args = args
value = args[0] if len(args) == 1 else kwargs['value'] if 'value' in kwargs.keys() else None
if value is None:
    if not hasattr(self, '__core__'): return f"{str(type(self))}@{id(self)}=Undefined#"
    elif self.__core__ is None: return f"{str(type(self))}@{id(self)}=None#"
    else: return f"{str(type(self))}@{id(self)}={self.__core__}#"
else: return f"{str(type(self))}@{id(self)}={value}#"